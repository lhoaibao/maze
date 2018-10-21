#!/usr/bin/env python3
import sys
import collections
alp = 'ASDFGHJKLQWERTYUIOPZXCVBNM'


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


def checkBonus(maze):
    for line in maze:
        if "!" in line:
            return True
    return False


# funtion read maze and return the position of A
def getPositionOfChar(maze, char):
    for line in maze:
        if char in line:
            return [line.index(char), maze.index(line)]
    return None


# funtion get the shortest way and return a list move
def bfs(maze, start, res):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if maze[y][x] == res:
            path.remove(path[0])
            return path
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if maze[y2][x2] != '#' and (x2, y2) not in seen:
                if maze[y2][x2] not in alp:
                    queue.append(path + [[x2, y2]])
                    seen.add((x2, y2))
    return None


# funtion return the command to move
def move(char, go):
    if go[1] - char[1] == 1:
        return "MOVE DOWN\n"
    elif go[1] - char[1] == -1:
        return "MOVE UP\n"
    elif go[0] - char[0] == 1:
        return "MOVE RIGHT\n"
    elif go[0] - char[0] == -1:
        return "MOVE LEFT\n"
    else:
        return None


def main():
    line = sys.stdin.readline()
    while line != "":
        if "HELLO" in line:
            print("I AM BAO\n")
        if "YOU ARE" in line:
            char = line[-2]
            print("OK\n")
        if "MAZE" in line:
            nowMaze = getMaze()
            nowPosition = getPositionOfChar(nowMaze, char)
            if checkBonus(nowMaze):
                move1 = bfs(nowMaze, (nowPosition[0], nowPosition[1]), '!')
                if move1 is None or len(move1) >= 20:
                    move1 = bfs(nowMaze, (nowPosition[0], nowPosition[1]), 'o')
            else:
                move1 = bfs(nowMaze, (nowPosition[0], nowPosition[1]), 'o')
            if move1 is None:
                move1 = bfs(nowMaze, (nowPosition[0], nowPosition[1]), ' ')
            print(move(nowPosition, move1[0]))
        line = sys.stdin.readline()


if __name__ == '__main__':
    main()
