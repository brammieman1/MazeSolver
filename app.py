import gen as gen
from flask import Flask, render_template, Response, jsonify
import functions as pfun
from camera_pi import Camera
import base_camera as base
# hoi
app = Flask(__name__)

CAPTURE, TRASH, START, RESET = "capture", "trash", "start", "reset"
AVAILABLE_COMMANDS = {
    'Capture': CAPTURE,
    'Trash': TRASH,
    'Start': START,
    'Rest': RESET
}

@app.route('/')
def execute():
    return render_template('index1.html', commands=AVAILABLE_COMMANDS)



def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/snapshot')
def snapshot():
    base.BaseCamera.thread.stop()
    print("I AM GOING TO TAKE A PICTURE BE WARNED")
    snapshot = pfun.picture();
    return jsonify({'snapshot': snapshot })
    #add return



@app.route('/data')
def data():
    mazeArray = pfun.convert().toList()
    print(mazeArray)
    return jsonify({'results': mazeArray})

    # return jsonify({'results': [
    # [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    #  [ 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    # [ 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    # [ 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    # [ 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
    # [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    # [ 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    # [ 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0],
    # [-1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
    # ]})


@app.route('/<cmd>')
def command(cmd=None):
    print (cmd)
    if cmd == RESET:
       camera_command = "X"
       response = "Resetting ..."
    else:
        camera_command = cmd[0].upper()
        response = "Moving {}".format(cmd.capitalize())
    return response, 200, {'Content-Type': 'text/plain'}




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')







