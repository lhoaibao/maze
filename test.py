#!/usr/bin/env python3
import sys
import collections


def getMaze():
    maze = []
    sys.stdin.readline()
    while True:
        line = sys.stdin.readline()
        if line[0] != "#":
            break
        maze.append(line)
    return maze


def getPositionOfA(maze):
    y = 0
    for line in maze:
        if "A" in line:
            x = line.index("A")
            return [y, x]
        else:
            y += 1


def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        y, x = path[-1]
        if grid[y][x] == 'o':
            path.remove(path[0])
            return path
        elif grid[y][x] == '!':
            path.remove(path[0])
            return path
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if grid[y2][x2] != '#' and (y2, x2) not in seen:
                queue.append(path + [[y2, x2]])
                seen.add((y2, x2))


def move(A, go):
    if go[1] - A[1] == 1:
        return "MOVE RIGHT\n\n"
    elif go[1] - A[1] == -1:
        return "MOVE LEFT\n\n"
    elif go[0] - A[0] == 1:
        return "MOVE DOWN\n\n"
    elif go[0] - A[0] == -1:
        return "MOVE UP\n\n"


line = sys.stdin.readline()
while line != "":
    if "HELLO" in line:
        sys.stdout.write("I AM BAO\n\n")
    if "YOU ARE A" in line:
        sys.stdout.write("OK\n\n")
    if "MAZE" in line:
        nowMaze = getMaze()
        nowPosition = getPositionOfA(nowMaze)
        move1 = bfs(nowMaze, (nowPosition[0], nowPosition[1]))
        sys.stdout.write(move(nowPosition, move1[0]))
    line = sys.stdin.readline()
