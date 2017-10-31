from queue import Queue

import numpy as np
import BlackWhite2 as bw

start = (170,170)
end = (171,171)

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
            return path

        for adjacent in getadjacent(current):
            #print(maze)
            x,y = adjacent
            if isZero(maze[x][y]):
                maze[x][y] = 2
                new_path = list(path)
                new_path.append(adjacent)
                queue.put(new_path)

    print("Queue is full! no answer")


if __name__ == "__main__":
    #anothermaze = bw.binarize_image('test.jpg',75)
    #print(anothermaze)
    numpymaze = np.array([(1, 1, 1, 1, 1), (1, 0, 0, 0, 1), (1, 1, 0, 1, 1), (1, 0, 0, 0, 1), (1, 1, 1, 1, 1)])

    path = BFS(start,end,numpymaze)

    for position in path:
          x,y = position
          numpymaze[x][y] = 3

    print(numpymaze.tolist())
    print("queued")