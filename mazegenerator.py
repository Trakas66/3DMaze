import random
import Settings

width, height = 20, 20
vWalls = [[1 for j in range(height)] for i in range(width+1)]
hWalls = [[1 for j in range(height+1)] for i in range(width)]
cells = [[0 for j in range(height)] for i in range(width)]


def makeMaze(current, cells, vWalls, hWalls):
    cells[current[0]][current[1]] = 1

    while True:
        possible = []
        if current[0]-1 >= 0 and cells[current[0]-1][current[1]] == 0:
            possible.append((current[0]-1, current[1]))
        if current[0]+1 < width and cells[current[0]+1][current[1]] == 0:
            possible.append((current[0]+1, current[1]))
        if current[1]-1 >= 0 and cells[current[0]][current[1]-1] == 0:
            possible.append((current[0], current[1]-1))
        if current[1]+1 < height and cells[current[0]][current[1]+1] == 0:
            possible.append((current[0], current[1]+1))

        if len(possible) == 0:
            return (cells, vWalls, hWalls)

        next = random.choice(possible)
        if next[0] == current[0]:
            if next[1] > current[1]:
                hWalls[next[0]][next[1]] = 0
            else:
                hWalls[next[0]][next[1]+1] = 0
        else:
            if next[0] > current[0]:
                vWalls[next[0]][next[1]] = 0
            else:
                vWalls[next[0]+1][next[1]] = 0

        cells, vWalls, hWalls = makeMaze(next, cells, vWalls, hWalls)


def solveMaze(start, end, cells, vWalls, hWalls):
    active = [start]
    explored = [start]
    path = {}

    while active:
        p = active.pop(0)
        possible = []

        if p == end:
            break

        if p[0]-1 >= 0 and vWalls[p[0]][p[1]] == 0:
            possible.append((p[0]-1, p[1]))
        if p[0]+1 < width and vWalls[p[0]+1][p[1]] == 0:
            possible.append((p[0]+1, p[1]))
        if p[1]-1 >= 0 and hWalls[p[0]][p[1]] == 0:
            possible.append((p[0], p[1]-1))
        if p[1]+1 < height and hWalls[p[0]][p[1]+1] == 0:
            possible.append((p[0], p[1]+1))

        for loc in possible:
            if loc not in explored:
                active.append(loc)
                explored.append(loc)
                path[loc] = p

    moves = 0
    current = end
    while True:
        if current not in path:
            break
        current = path[current]
        moves += 1
    return moves


def checkSurr(vWalls, hWalls, i, j):
    count = 0
    w = width*2+1
    h = height*2+1
    if i - 1 >= 0 and hWalls[(i-1)//2][j//2] == 1:
        count += 1
    if i + 1 < w and hWalls[(i+1)//2][j//2] == 1:
        count += 1
    if j - 1 >= 0 and vWalls[i//2][(j-1)//2] == 1:
        count += 1
    if j + 1 < h and vWalls[i//2][(j+1)//2] == 1:
        count += 1
    return count


def mazeArray():
    global cells, vWalls, hWalls
    while True:
        start = (random.randint(0, width - 1), random.randint(0, height - 1))
        cells, vWalls, hWalls = makeMaze(start, cells, vWalls, hWalls)
        #print(solveMaze(start, (7, 0), cells, hWalls, vWalls))
        if solveMaze(start, (7, 0), cells, hWalls, vWalls) == 0:
            break
        else:
            vWalls = [[1 for j in range(height)] for i in range(width + 1)]
            hWalls = [[1 for j in range(height + 1)] for i in range(width)]
            cells = [[0 for j in range(height)] for i in range(width)]

    arr = [[0 for j in range(height*2+1)] for i in range(width*2+1)]
    for i in range(width*2+1):
        for j in range(height*2+1):
            if i % 2 == 1 and j % 2 == 1:
                arr[i][j] = 0
            elif i % 2 == 0 and j % 2 == 1:
                arr[i][j] = vWalls[i//2][j//2]
            elif i % 2 == 1 and j % 2 == 0:
                arr[i][j] = hWalls[i//2][j//2]
            else:
                if checkSurr(vWalls, hWalls, i, j) > 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = 0
    arr[0][15] = 0
    Settings.PLAYER_POS = start[0]*2+1.5, start[1]*2+1.5
    return arr