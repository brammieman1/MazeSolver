import gen as gen
from flask import Flask, render_template, Response, jsonify, request
# import functions as pfun
# from camera_pi import Camera
import BFS as bfs
import numpy as np
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

@app.route('/sendMaze', methods = ['POST'])
def get_post_javascript_data():
    maze = request.form['maze']
    startx = int(request.form['startx'])
    starty = int(request.form['starty'])
    endx = int(request.form['endx'])
    endy = int(request.form['endy'])
    print("i am alive")
    start = (starty,startx)
    end = (endy,endx)
    print(maze)
    print(start,end)
    resultaat = bfs.BFS(start, end, bfs.arrayCoverting(maze))
    print("de vogel is gevolgen")
    print(resultaat)

    solvedArray = resultaat.tolist()
    return jsonify({'solutions': solvedArray})






@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/snapshot')
def snapshot():
    Camera.StopPreview()
    print("I AM GOING TO TAKE A PICTURE BE WARNED")
    snapshot = pfun.picture()
    return jsonify({'snapshot': snapshot })
    #add return



@app.route('/data')
def data():
    mazeArray = pfun.convert().tolist()
    return jsonify({'results': mazeArray})

    # return jsonify({'results': [
    # [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    # [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    # [ 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    # [ 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    # [ 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    # [ 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
    # [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    # [ 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    # [ 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0],
    # [ 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
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







