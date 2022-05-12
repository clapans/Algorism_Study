import sys

n = int(sys.stdin.readline())
dx = [0,-1,0,1]
dy = [1,0,-1,0]
square = [[0]*101 for _ in range(101)]
res = 0

def makeDragon(x,y,dirs,g,cnt):
    if g > cnt:
        new_dirs = []
        for i in range(len(dirs),0,-1):
            if dirs[i-1] == 3:
                new_dirs.append(0)
            else:
                new_dirs.append(dirs[i-1] + 1)
            x += dx[new_dirs[-1]]
            y += dy[new_dirs[-1]]
            square[x][y] = 1
        new_dirs = dirs + new_dirs
        makeDragon(x,y,new_dirs,g,cnt + 1)

def isDragon(x,y):
    for i in range(x,x+2):
        for j in range(y,y+2):
            if square[i][j] == 0:
                return False
    return True

for _ in range(n):
    y,x,d,g = map(int,sys.stdin.readline().split())
    square[x][y] = 1
    x += dx[d]
    y += dy[d]
    square[x][y] = 1
    makeDragon(x,y,[d],g,0)

for i in range(100):
    for j in range(100):
        if isDragon(i,j):
            res += 1

print(res)