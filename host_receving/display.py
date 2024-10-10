"""
    Read and display video input from redis server 
"""
import redis 
import cv2 
import numpy as np 

STANFORD_KEY_1 = 'stanford_1/image'
STANFORD_KEY_2 = 'stanford_2/image'
STANFORD_KEY_3 = 'stanford_3/image'
DLR_KEY = 'dlr/image'
SNU_KEY = 'snu/imge'
NUS_KEY = 'nus/image'
REMOTE_IP = '127.0.0.1'
PORT = 6379
r = redis.Redis(host = REMOTE_IP, port = PORT, decode_responses = False)

if __name__ == "__main__":
    running = True

    while running:
        # byte_data = r.get('realsense::rgb')
        byte_data = r.get(STANFORD_KEY_1)
        np_byte_data = np.fromstring(byte_data, np.uint8)
        img = cv2.imdecode(np_byte_data, cv2.IMREAD_COLOR) # 0.015 sec
        # img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        # rotated_image = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imshow('Image', img)
        
        # Wait for key press (30 ms)
        key = cv2.waitKey(30)
        
        # Check if 'q' key is pressed to quit
        if key & 0xFF == ord('q'):
            running = False