"""
    Grab images and send to server 
"""
from flask import Flask, Response
import cv2
import numpy as np
import redis
import time

STANFORD_KEY_1 = 'stanford/image/1'
STANFORD_KEY_2 = 'stanford/image/2'
STANFORD_KEY_3 = 'stanford/image/3'
DLR_KEY = 'dlr/image'
SNU_KEY = 'snu/imge'
NUS_KEY = 'nus/image'

app = Flask(__name__)

REMOTE_IP = '127.0.0.1'
PORT = 6379
redis_client = redis.Redis(host = REMOTE_IP, port = PORT, decode_responses = False)

def generate_frames(key):
    while True:
        # Fetch image data from Redis
        image_data = redis_client.get(key)  # Replace 'image_key' with your actual key
        
        # Yield the frame as bytes for streaming
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + image_data + b'\r\n')

        # Add a delay to control the frame rate
        time.sleep(0.01)  # Adjust this value as needed

@app.route('/stanford_1')
def video_feed_1():
    return Response(generate_frames(STANFORD_KEY_1),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
@app.route('/stanford_2')
def video_feed_2():
    return Response(generate_frames(STANFORD_KEY_2),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stanford_3')
def video_feed_3():
    return Response(generate_frames(STANFORD_KEY_3),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/dlr')
def video_feed_4():
    return Response(generate_frames(DLR_KEY),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/snu')
def video_feed_5():
    return Response(generate_frames(SNU_KEY),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/nus')
def video_feed_6():
    return Response(generate_frames(NUS_KEY),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, threaded=True)
