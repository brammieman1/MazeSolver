import io
import time
import picamera
from base_camera import BaseCamera

output = './static/images/output.jpg'

class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            camera.resolution = (320, 240)
            # let camera warm up
            time.sleep(2)

            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()

    @staticmethod
    def takepicture():
        BaseCamera.close()
        print('basdjfkasdjfkasdjfalksdfjkasdjfl')
        with picamera.PiCamera() as camera:
            camera.framerate = 24
            time.sleep(2)
            camera.capture(output)
            print('picture taken')
            return output
