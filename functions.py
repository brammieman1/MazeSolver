
from io import BytesIO
import time
import picamera
import numpy as np
import BlackWhite2
from PIL import Image
import shutil
import time
import sqlite3
import app

conn = None

def picture():
   time.sleep(1)
   with picamera.PiCamera() as camera:
       camera.framerate = 24
       camera.resolution = (640, 480)
       time.sleep(2)
       camera.capture(output)
       print('picture taken')
       return output

def copypasta(name):
    timestamp = str(time.time())
    puzzlename = name
    newoutput = './static/images' + timestamp + '.jpg'
    shutil.copyfile(output, newoutput)


def convert():
   return BlackWhite2.binarize_image(output, 75)


def insertImage(id,name, path):
    conn = sqlite3.connect('maze.db')
    print("connection openend")
    if (conn is not None):
        conn.execute("INSERT INTO test (name,path) VALUES (?,?)"(name,path))
    else:
        print("First open connection!")


def createDatabase():
    conn.execute('''CREATE TABLE mazes(
                  id INTEGER AUTOINCREMENT  )''')
output = './static/images/output.jpg'

if __name__ == "__main__":
    copypasta("Baap")