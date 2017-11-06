from queue import Queue

import numpy as np
import BlackWhite2 as bw

start = (1,1)
end = (3,3)

def isZero(value):
    if value == 0:
        return True

def getadjacent(n):
    x,y = n
    return [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]

def BFS(start,end, maze):
    queue = Queue()
    queue.put([start])

    while not queue.empty():
        path = queue.get()
        current = path[-1]

        if current == end:
            for position in path:
                #print(position)
                x, y = position
                maze[x][y] = 3
            return maze

        for adjacent in getadjacent(current):
            x,y = adjacent
            if isZero(maze[x][y]):
                maze[x][y] = 2
                new_path = list(path)
                new_path.append(adjacent)
                queue.put(new_path)

    print("Queue is full! no answer")
    return maze




def arrayCoverting(string):
    matrixAr = []
    mystring = string
    b = mystring.replace("[[", "").replace("]]", "")  # to remove head [[ and tail ]]
    for line in b.split('],['):
        row = list(
            map(int, line.split(',')))  # map = to convert the number from string (some has also space ) to integer
        matrixAr.append(row)
    numpyArray = np.array(matrixAr)
    return numpyArray

if __name__ == "__main__":
    # anothermaze = bw.binarize_image('test.jpg',150)
    # #print(anothermaze)
    # numpymaze = np.array([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 0, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]])
    # print(numpymaze)

    baap = np.array([[1,1,1,1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,0,1],[1,0,1,0,0,0,0,0,1,0,1],[1,0,0,0,1,1,1,0,1,0,1],[1,1,1,0,0,0,1,0,1,0,1],[1,0,1,1,1,1,1,0,1,0,1],[1,0,1,0,0,0,1,0,1,0,1],[1,0,1,0,1,0,1,0,0,0,1],[1,0,0,0,1,0,0,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1]])
    oplossing = BFS((1,1),(9,1),baap)
    print(oplossing)
    # puzzel = (arrayCoverting("[[1,1,1,1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,0,1],[1,0,1,0,0,0,0,0,1,0,1],[1,0,0,0,1,1,1,0,1,0,1],[1,1,1,0,0,0,1,0,1,0,1],[1,0,1,1,1,1,1,0,1,0,1],[1,0,1,0,0,0,1,0,1,0,1],[1,0,1,0,1,0,1,0,0,0,1],[1,0,1,0,1,0,0,1,1,0,1],[1,1,1,1,1,1,1,1,1,1,1]]"))
    # oplossing = BFS((1,1),(9,9),puzzel)
    # print(oplossing)
    #path = BFS(start,end,numpymaze)
    #drawpath(path);
    #print(numpymaze)
    #print(numpymaze.tolist())
    #print("queued")