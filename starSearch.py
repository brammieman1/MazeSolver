import heapq
import sys

import numpy as np

#maze = np.array([[]])


def AStar(start, goal, neighbor_nodes, dist_between, heuristic_cost_estimate):



    def reconstruct_path(came_from, current_node):
        path = [current_node]
        while current_node in came_from:
            current_node = came_from[current_node]
            path.append(current_node)
        return list(reversed(path))

    g_score = {start: 0}
    f_score = {start: g_score[start] + heuristic_cost_estimate(start, goal)}
    openheap = [(f_score[start], start)]
    openset = {start}
    closedset = set()
    came_from = dict()

    while openset:
        _, current = heapq.heappop(openheap)
        openset.remove(current)
        if current == goal:
            return reconstruct_path(came_from, goal)
        closedset.add(current)
        for neighbor in neighbor_nodes(current):
            tentative_g_score = (
                g_score[current] + dist_between(current, neighbor)
            )
            if neighbor in closedset and tentative_g_score >= g_score[neighbor]:
                continue
            if neighbor not in openset or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                # TODO: there might be an implementation error:
                # is the heap updated when the f_score of a node is changed?
                f_score[neighbor] = (
                    g_score[neighbor] + heuristic_cost_estimate(neighbor, goal)
                )
                if neighbor not in openset:
                    heapq.heappush(openheap, (f_score[neighbor], neighbor))
                    openset.add(neighbor)
    print("no path found :(")

def is_blocked(p):
    x,y = p
    if maze[x,y] == 1:
        return True

def von_neumann_neighbors(p):
    x,y = p

    neighbors = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
    return [p for p in neighbors if not is_blocked(p)]
def manhattan(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
def squared_euclidean(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def ready(puzzle, start, end):
    start = start
    goal = end
    global maze
    maze = puzzle
    #print(maze)
    path = AStar(start,goal,von_neumann_neighbors, manhattan,manhattan)
    for position in path:
        x,y = position
        maze[x,y] = 3 #red
    #print(maze)
    return maze

if __name__ == '__main__':
    puzzle = np.array([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 0, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]])
    start = (1,1)
    goal = (3,3)
    ready(puzzle,start, goal)
