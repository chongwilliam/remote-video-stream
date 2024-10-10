"""
    Stream video input to redis server
"""
import redis 
import cv2 

STANFORD_KEY_1 = 'stanford/image/1'
STANFORD_KEY_2 = 'stanford/image/2'
STANFORD_KEY_3 = 'stanford/image/3'
DLR_KEY = 'dlr/image'
SNU_KEY = 'snu/imge'
NUS_KEY = 'nus/image'

REMOTE_IP = '127.0.0.1'
PORT = 6379
r = redis.Redis(host = REMOTE_IP, port = PORT, decode_responses = True)

if __name__ == '__main__':
    
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Could not open webcam")
    else:
        print("Starting video stream")
        while True:
            # Grab rgb input 
            ret, frame = cap.read()
            
            # Convert to bit
            _, jpeg_encoded = cv2.imencode('.jpg', frame)
            
            # Publish JPEG image to redis 
            r.set(STANFORD_KEY_1, jpeg_encoded.tobytes())
            r.set(STANFORD_KEY_2, jpeg_encoded.tobytes())
            r.set(STANFORD_KEY_3, jpeg_encoded.tobytes())
            r.set(DLR_KEY, jpeg_encoded.tobytes())
            r.set(SNU_KEY, jpeg_encoded.tobytes())
            r.set(NUS_KEY, jpeg_encoded.tobytes())
