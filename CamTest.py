import os
import time
try1 = []

def capture():
    os.system('fswebcam home/pi/ExperimentTest/camworks.jpg')
    print("Photo clicked")
    try1.append("camworks.jpg")
    time.sleep(10)
    
b=capture()
