
from io import BytesIO
import time
import picamera
import numpy as np
import BlackWhite2
from PIL import Image

output = '/static/images/output.jpg'

def picture():
   with picamera.PiCamera() as camera:
       camera.framerate = 24
       time.sleep(2)
       camera.capture(output)
       print('picture taken')
       return output


def convert(image):
   return BlackWhite2.binarize_image(output, 75)
