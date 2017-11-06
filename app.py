import gen as gen
import shutil
from flask import Flask, render_template, Response, jsonify, request
import functions as pfun
from camera_pi import Camera
import BFS as bfs
import numpy as np
import sqlite3
import time
import starSearch

# hoi
app = Flask(__name__)

CAPTURE, TRASH, START, RESET, HISTORY = "capture", "trash", "start", "reset", "history"
AVAILABLE_COMMANDS = {
    'Capture': CAPTURE,
    'Trash': TRASH,
    'Start': START,
    'Reset': RESET,
    'History': HISTORY
}

output = './MazeSolver/static/images/output.jpg'

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
    method = 1;
    method = request.form['algorithm']
    maze = request.form['maze']
    startx = int(request.form['startx'])
    starty = int(request.form['starty'])
    endx = int(request.form['endx'])
    endy = int(request.form['endy'])
    start = (starty,startx)
    end = (endy,endx)
    #maze = bfs.arrayCoverting(maze)
    print(maze)
    if (method == 0): #BFS
        maze = bfs.arrayCoverting(maze)
        solved = bfs.bfs(maze)
        solved = maze.tolist()
        return jsonify({'solutions': solved})
    if (method == 1): #a-starSearch
        maze = bfs.arrayCoverting(maze)
        solved = starSearch.ready(maze, start, end)
        solved = maze.tolist()
        return jsonify({'solutions': solved})
    if (method == 3): #anh deel
        #communicatie aanroepen!
        return "not yet implemented"
    else:
        return None


@app.route('/saveMaze', methods = ['POST'])
def get_post_javascript_saveMaze():
    name = request.form['name']
    insertImage(name)
    return "Save completed"

@app.route('/deleteMaze', methods=['POST'])
def get_post_javascript_delete():
    mid = request.form['mid']
    return "Delete completed"

@app.route('/DBdata')
def DBdata():
    DBresults = getPuzzles()
    return jsonify({'DBresults': DBresults})



def insertImage(name):
    timestamp = str(time.time())
    puzzlename = name
    newoutput = './MazeSolver/static/images' + timestamp + '.jpg'
    shutil.copyfile(output, newoutput)
    conn = sqlite3.connect('./maze.db')
    c = conn.cursor()
    # c.execute("CREATE TABLE puzzle (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, path TEXT)")
    c.execute("INSERT INTO puzzle(name,path) VALUES(?,?)",(puzzlename,newoutput))
    conn.commit()
    conn.close()

def getPuzzles():
    conn = sqlite3.connect('./MazeSolver/maze.db')
    c = conn.cursor()
    c.execute("SELECT name, path FROM puzzle ORDER BY id DESC")
    print(c.fetchall())
    conn.commit()
    conn.close()
    return None

def removePuzzle(id):
    conn = sqlite3.connect('./MazeSolver/maze.db')
    c = conn.cursor()
    c.execute("DELETE FROM puzzle WHERE id = (?)",(id))
    conn.commit()
    conn.close()


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
    #insertImage("Baap")
    #getPuzzles()
    app.run(debug=True, host='0.0.0.0')







