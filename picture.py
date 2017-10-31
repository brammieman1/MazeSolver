import time
import picamera
import numpy as np
import BlackWhite2
from PIL import Image

with picamera.PiCamera() as camera:
    camera.resolution = (320,240)
    camera.framerate = 24
    time.sleep(2)
    output = np.empty((240,320, 3), dtype = np.uint8)
    camera.color_effects = (128,128)
    camera.capture(output, 'rgb')
    print(output)
    img = Image.fromarray(output, 'RGB')
    img.save('my.png')
    outputnew = BlackWhite2.binarize_array(output, 75)
    print(outputnew)
