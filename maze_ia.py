#!/usr/bin/env python3
import sys
import collections


# funtion read maze every time it change
def getMaze():
    maze = []  # list variable to store the maze
    sys.stdin.readline()
    while True:
        line = sys.stdin.readline()
        if line[0] != "#":
            break
        maze.append(line)  # and the line are reading to the list maze
    return maze  # return the maze for use


# funtion check the bonus point is in maze
def checkBonus(maze):
    for line in maze:
        if "!" in line:
            return True  # if yes
    return False  # if no


# funtion read maze and return the position of A
def getPositionOfChar(maze, char):
    for line in maze:  # read every element in list maze
        if char in line:
            # if player is in maze return position of player
            return [line.index(char), maze.index(line)]
    return None  # else return None


# funtion get the shortest way and return a list move
def bfs(maze, start, res):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]  # add position to tail
        if maze[y][x] == res:  # if this position meet resouces
            path.remove(path[0])  # remove now position of player in list move
            return path  # and return the list move
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            # if position of 4 direction of player is not "#" and haven't go
            if maze[y2][x2] != '#' and (x2, y2) not in seen:
                # and if these position is not opponent player
                if maze[y2][x2] not in 'ASDFGHJKLQWERTYUIOPZXCVBNM':
                    # add this position to list move and set seen
                    queue.append(path + [[x2, y2]])
                    seen.add((x2, y2))
    return None  # if can't find out the way to resouces return None


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
            nowMaze = getMaze()  # get the maze at now
            # get position of this player at now
            nowPosition = getPositionOfChar(nowMaze, char)
            if checkBonus(nowMaze):  # if resouces bonus in maze
                # fine the shortest move to this resouces
                move1 = bfs(nowMaze, (nowPosition[0], nowPosition[1]), '!')
                if move1 is None or len(move1) >= 20:
                    # if can't move to bonus resouces or length of move to this
                    # resouces is over 20
                    # find the shortest move to normal resouces
                    move1 = bfs(nowMaze, (nowPosition[0], nowPosition[1]), 'o')
            else:
                move1 = bfs(nowMaze, (nowPosition[0], nowPosition[1]), 'o')
            if move1 is None:
                move1 = bfs(nowMaze, (nowPosition[0], nowPosition[1]), ' ')
            print(move(nowPosition, move1[0]))
        line = sys.stdin.readline()


if __name__ == '__main__':
    main()
