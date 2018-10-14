#!/usr/bin/env python3
import sys
import collections

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

def bfs(grid, start):
  queue = collections.deque([[start]])
  seen = set([start])
  while queue:
      path = queue.popleft()
      y, x = path[-1]
      if grid[y][x] == 'o':
          return path
      for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
          if 0 <= x2 < len(maze[0]) and 0 <= y2 < len(maze) and grid[y2][x2] != '#' and (y2, x2) not in seen:
              queue.append(path + [[y2, x2]])
              seen.add((y2, x2))
def move():
    getMaze()
    getPositionOfA()
    move = bfs(maze,APosition)
    if move[1] == APosition[1] +1:
        print("MOVE DOWN\n")
    if move[1] == APosition[1] -1:
        print("MOVE UP\n")
    if move[0] == APosition[0] +1:
        print("MOVE RIGHT\n")
    if move[0] == APosition[0] -1:
        print("MOVE LEFT\n")


move()
