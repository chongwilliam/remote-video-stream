from flask import Flask, Response
import redis
import cv2 
import numpy as np 
import threading

app1 = Flask(__name__)
app2 = Flask(__name__)
app3 = Flask(__name__)
app4 = Flask(__name__)
app5 = Flask(__name__)
app6 = Flask(__name__)

STANFORD_KEY_1 = 'stanford/image/1'
STANFORD_KEY_2 = 'stanford/image/2'
STANFORD_KEY_3 = 'stanford/image/3'
DLR_KEY = 'dlr/image'
SNU_KEY = 'snu/imge'
NUS_KEY = 'nus/image'
REMOTE_IP = '127.0.0.1'
PORT = 6379
r = redis.Redis(host = REMOTE_IP, port = PORT, decode_responses = False)

@app1.route('/image/stanford_1')
def get_image_1():
    # img = r.get('image_key')
    byte_data = r.get(STANFORD_KEY_1)
    # np_byte_data = np.fromstring(byte_data, np.uint8)
    # img = cv2.imdecode(np_byte_data, cv2.IMREAD_COLOR) # 0.015 sec
    return Response(byte_data, mimetype='image/jpeg')

@app2.route('/image/stanford_2')
def get_image_2():
    # img = r.get('image_key')
    byte_data = r.get(STANFORD_KEY_2)
    # np_byte_data = np.fromstring(byte_data, np.uint8)
    # img = cv2.imdecode(np_byte_data, cv2.IMREAD_COLOR) # 0.015 sec
    return Response(byte_data, mimetype='image/jpeg')

@app3.route('/image/stanford_3')
def get_image_3():
    # img = r.get('image_key')
    byte_data = r.get(STANFORD_KEY_3)
    # np_byte_data = np.fromstring(byte_data, np.uint8)
    # img = cv2.imdecode(np_byte_data, cv2.IMREAD_COLOR) # 0.015 sec
    return Response(byte_data, mimetype='image/jpeg')

@app4.route('/image/dlr')
def get_image_4():
    # img = r.get('image_key')
    byte_data = r.get(DLR_KEY)
    # np_byte_data = np.fromstring(byte_data, np.uint8)
    # img = cv2.imdecode(np_byte_data, cv2.IMREAD_COLOR) # 0.015 sec
    return Response(byte_data, mimetype='image/jpeg')

@app5.route('/image/snu')
def get_image_5():
    # img = r.get('image_key')
    byte_data = r.get(SNU_KEY)
    # np_byte_data = np.fromstring(byte_data, np.uint8)
    # img = cv2.imdecode(np_byte_data, cv2.IMREAD_COLOR) # 0.015 sec
    return Response(byte_data, mimetype='image/jpeg')

@app6.route('/image/nus')
def get_image_6():
    # img = r.get('image_key')
    byte_data = r.get(NUS_KEY)
    # np_byte_data = np.fromstring(byte_data, np.uint8)
    # img = cv2.imdecode(np_byte_data, cv2.IMREAD_COLOR) # 0.015 sec
    return Response(byte_data, mimetype='image/jpeg')

def run_1():
    app1.run(host='0.0.0.0', port=4444, threaded=True)
    
def run_2():
    app2.run(host='0.0.0.0', port=4445, threaded=True)

if __name__ == '__main__':
    threads = []
    # app1.run(host='0.0.0.0', port=4444, threaded=True)
    # app2.run(host='0.0.0.0', port=4444, threaded=True)
    # app3.run(host='0.0.0.0', port=4444, threaded=True)
    # app4.run(host='0.0.0.0', port=4444, threaded=True)
    # app5.run(host='0.0.0.0', port=4444, threaded=True)
    # app6.run(host='0.0.0.0', port=4444, threaded=True)
    
    # Create threads
    thread1 = threading.Thread(target=run_1)
    # thread2 = threading.Thread(target=run_2)

    # Start threads
    thread1.start()
    # thread2.start()

    # Wait for both threads to finish
    thread1.join()
    # thread2.join()
