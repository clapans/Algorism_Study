import sys

r,c,t = map(int,sys.stdin.readline().split())
dustArr = []
dustList = []
inverseCycle = []
normalCycle = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(r):
    dustArr.append(list(map(int,sys.stdin.readline().split())))

def checkDust():
    for i in range(r):
        for j in range(c):
            if dustArr[i][j] > 0:
                dustList.append([i,j,dustArr[i][j]//5])

def spread():
    global dustList
    for dust in dustList:
        cnt = 0
        for i in range(4):
            x = dust[0] + dx[i]
            y = dust[1] + dy[i]
            if 0 <= x < r and 0 <= y < c and dustArr[x][y] > -1:
                dustArr[x][y] += dust[2]
                cnt += 1
        dustArr[dust[0]][dust[1]] -= dust[2]*cnt
    dustList = []

def clean(lst):
    for i in range(1,len(lst)):
        pre_x,pre_y = lst[i-1][0],lst[i-1][1]
        x,y = lst[i][0],lst[i][1]
        dustArr[pre_x][pre_y] = dustArr[x][y]
        if i == len(lst)-1:
            dustArr[x][y] = 0

isInverse = True

for i in range(r):
    for j in range(c):
        if dustArr[i][j] == -1:
            if isInverse:
                isInverse = False
                for k in range(i-1,0,-1):
                    inverseCycle.append([k,j])
                for k in range(c-1):
                    inverseCycle.append([0,k])
                for k in range(i):
                    inverseCycle.append([k,c-1])
                for k in range(c-1,0,-1):
                    inverseCycle.append([i,k])
            else:
                for k in range(i+1,r-1):
                    normalCycle.append([k,j])
                for k in range(c-1):
                    normalCycle.append([r-1,k])
                for k in range(r-1,i,-1):
                    normalCycle.append([k,c-1])
                for k in range(c-1,0,-1):
                    normalCycle.append([i,k])

for i in range(t):
    checkDust()
    spread()
    clean(inverseCycle)
    clean(normalCycle)

cnt = 0

for i in range(r):
    for j in range(c):
        if dustArr[i][j] > 0:
            cnt += dustArr[i][j]

print(cnt)