from io import BytesIO
import time
import picamera
import numpy as np
import BlackWhite2
from PIL import Image

output = 'output.jpg'

def getArray():
    with picamera.PiCamera() as camera:
       camera.framerate = 24
       time.sleep(2)
       camera.capture(output)
       print('picture taken')
       outputnew = BlackWhite2.binarize_image(output, 75)
       print(outputnew)
       return outputnew

if __name__ == "__main__":
    getArray()


