#!/usr/bin/env python3
import sys
import math

# make a list to store maze
maze = []
APosition = []
CoinPosition = []
SpecialCoinPosition = []
target = []

sys.stdin.readline()
sys.stdin.readline()
print("I AM BAO\n")
sys.stdin.readline()
sys.stdin.readline()
print("OK\n")
sys.stdin.readline()


#function get now board
def getMaze():
    maze.clear()
    line = sys.stdin.readline()
    maze.append(line)
    while True:
        line = sys.stdin.readline()
        if line == maze[0]:
            maze.append(line)
            break
        maze.append(line)


def distance(A,B):
    return math.sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2)


def getPositionOfA():
    APosition.clear()
    y = 0
    for line in maze:
        if "A" in line:
            x = line.index("A")
            APosition.extend([x,y])
            break
        else:
            y+=1

def getPositionOfCoin():
    y = 0
    CoinPosition.clear()
    for line in maze:
        if "o" in line:
            for x in range(len(line)):
                if(line[x] == "o"):
                    CoinPosition.append([x,y])
        else:
            y+=1
    y = 0
    SpecialCoinPosition.clear()
    for line in maze:
        if "!" in line:
            for x in range(len(line)):
                if(line[x] == "!"):
                    CoinPosition.append([x,y])
        else:
            y+=1


def shortestMove():
    if(len(SpecialCoinPosition)!=0):
        min = distance(SpecialCoinPosition[0], APosition)
        for item in SpecialCoinPosition:
            if distance(item,APosition) <= min:
                target.clear()
                target.extend(item)
                min = distance(item,APosition)
        return min
    else:
        min = distance(CoinPosition[0], APosition)
        for item in CoinPosition:
            if distance(item,APosition) <= min:
                target.clear()
                target.extend(item)
                min = distance(item,APosition)
        return min

def move():
    getMaze()
    getPositionOfA()
    getPositionOfCoin()
    minWay = shortestMove()
    if maze[APosition[0]][APosition[1]-1] != "#":
        if distance([APosition[0],APosition[1]-1],target)<minWay:
            print("MOVE UP\n")
    if maze[APosition[0]][APosition[1]+1] != "#":
        if distance([APosition[0],APosition[1]-1],target)<minWay:
            print("MOVE DOWN\n")
    if maze[APosition[0]-1][APosition[1]] != "#":
        if distance([APosition[0],APosition[1]-1],target)<minWay:
            print("MOVE LEFT\n")
    if maze[APosition[0]+1][APosition[1]] != "#":
        if distance([APosition[0],APosition[1]-1],target)<minWay:
            print("MOVE RIGHT\n")
while True:
    move()
    line = sys.stdin.readline()
