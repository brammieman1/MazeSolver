from io import BytesIO
import time
import picamera
import numpy as np
import BlackWhite2
from PIL import Image

output = 'output.jpg'

with picamera.PiCamera() as camera:
  #  stream = BytesIO()
   # camera.start_preview()
   # time.sleep(2)
 #   camera.capture(stream, format='jpeg')
    # "Rewind" the stream to the beginning so we can read its content
  #  stream.seek(0)
 #   image = Image.open(stream)
 #   camera.resolution = (320,240)
    camera.framerate = 24
    time.sleep(2)
  #  output = np.empty((240,320, 3), dtype = np.uint8)
  #  camera.color_effects = (128,128)
    camera.capture(output)
    print('picture taken')
    outputnew = BlackWhite2.binarize_image(output, 75)
    print(outputnew)
