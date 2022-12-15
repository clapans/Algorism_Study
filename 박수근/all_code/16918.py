r,c,n = map(int,input().split())

explode = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def spendTime():
    isExplode = []
    for i in range(r):
        for j in range(c):
            if explode[i][j]:
                if explode[i][j] == 1:
                    isExplode.append([i,j])
                explode[i][j] -= 1 
    return isExplode

def plantBomb():
    for i in range(r):
        for j in range(c):
            if not explode[i][j]:
                explode[i][j] = 4

def explodedBomb(bombList):
    for bomb in bombList:
        x,y = bomb
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < r and 0 <= ny < c and explode[nx][ny] != 0:
                explode[nx][ny] = 0
            
for _ in range(r):
    arr = []
    for t in list(input()):
        if t == 'O':
            arr.append(2)
        else:
            arr.append(0)
    explode.append(arr)

if n == 1:
    for i in range(r):
        for j in range(c):
            if explode[i][j] == 2:
                print('O',end='')
            else:
                print('.',end='')
        print('')
else:
    for _ in range(n-1):
        plantBomb()
        explodedBomb(spendTime())

    for i in range(r):
        for j in range(c):
            if explode[i][j] == 0:
                print('.',end='')
            else:
                print('O',end='')
        print('')