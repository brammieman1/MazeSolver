import numpy as np


def visited(x,y):
    numpymaze[x][y] = 2

def checkNeighbours(x,y):
    if(numpymaze[x+1][y] == 0):
        return [x+1,y]
    elif(numpymaze[x-1][y] == 0):
        return [x-1,y]
    elif(numpymaze[x][y+1] == 0):
        return [x,y+1]
    elif(numpymaze[x][y-1] == 0):
        return [x,y-1]
    else:
        return backtrack(x,y)

def backtrack(x,y):
    if (numpymaze[x + 1][y] == 2):
        return [x + 1, y]
    elif (numpymaze[x - 1][y] == 2):
        return [x - 1, y]
    elif (numpymaze[x][y + 1] == 2):
        return [x,y + 1]
    elif (numpymaze[x][y - 1] == 2):
        return [x,y - 1]


if __name__ == "__main__":
    numpymaze = np.array([(1, 1, 1, 1, 1), (1, 0, 0, 0, 1), (1, 1, 0, 1, 1), (1, 0, 0, 0, 1), (1, 1, 1, 1, 1)])
    startposition = [1, 1]
    endposition = [3, 3]
    #finished = False
    currentelement = startposition


    visited(startposition[0],startposition[1])

    while (True):
        print(currentelement)
        currentelement = checkNeighbours(currentelement[0],currentelement[1])
        print(currentelement)
        visited(currentelement[0],currentelement[1])
        if (currentelement == endposition):
            print("klaar")
            break;

        print(numpymaze)

print(numpymaze)
