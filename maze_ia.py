#!/usr/bin/env python3
import sys
import collections


# funtion read maze every time it change
def getMaze():
    maze = []
    sys.stdin.readline()
    while True:
        line = sys.stdin.readline()
        if line[0] != "#":
            break
        maze.append(line)
    return maze


# funtion read maze and return the position of A
def getPositionOfA(maze):
    y = 0
    for line in maze:
        if "A" in line:
            x = line.index("A")
            return [x, y]
        else:
            y += 1


# funtion get the shortest way and return a list move
def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == 'o':
            path.remove(path[0])
            return path[0]
        elif grid[y][x] == '!':
            path.remove(path[0])
            return path[0]
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if grid[y2][x2] != '#' and (x2, y2) not in seen:
                queue.append(path + [[x2, y2]])
                seen.add((x2, y2))


# funtion return the command to move
def move(A, go):
    if go[1] - A[1] == 1:
        return "MOVE DOWN\n"
    elif go[1] - A[1] == -1:
        return "MOVE UP\n"
    elif go[0] - A[0] == 1:
        return "MOVE RIGHT\n"
    elif go[0] - A[0] == -1:
        return "MOVE LEFT\n"


# run here
line = sys.stdin.readline()
while line != "":
    if "HELLO" in line:
        print("I AM BAO\n")
    if "YOU ARE A" in line:
        print("OK\n")
    if "MAZE" in line:
        nowMaze = getMaze()
        nowPosition = getPositionOfA(nowMaze)
        move1 = bfs(nowMaze, (nowPosition[0], nowPosition[1]))
        print(move(nowPosition, move1))
    line = sys.stdin.readline()
