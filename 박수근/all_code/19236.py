import sys

arr = [[0]*4 for _ in range(4)]
dx = [0,-1,-1,0,1,1,1,0,-1]
dy = [0,0,-1,-1,-1,0,1,1,1]
res = 0

def moveOrder(s):
    global res
    for t in range(1,17):
        move(t)
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == -1:
                fishLst = fishList([i,j])
                tmp = [i,j]
    
    arrSave = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            arrSave[i][j] = [arr[i][j][0],arr[i][j][1]]
    if fishLst:
        for fish in fishLst:
            fishSave = [arr[fish[0]][fish[1]][0],arr[fish[0]][fish[1]][1]]
            arr[fish[0]][fish[1]][0] = -1
            arr[tmp[0]][tmp[1]] = [0,0]
            moveOrder(s+fishSave[0])
            for i in range(4):
                for j in range(4):
                    arr[i][j] = [arrSave[i][j][0],arrSave[i][j][1]]
    else:
        res = max(res,s)
        
def move(num):
    for x in range(4):
        for y in range(4):
            if arr[x][y][0] == num:
                cnt = 0
                while cnt < 8:
                    nx = x + dx[arr[x][y][1]]
                    ny = y + dy[arr[x][y][1]]
                    if 0 <= nx < 4 and 0 <= ny < 4 and arr[nx][ny][0] > -1:
                        tmp = [arr[nx][ny][0],arr[nx][ny][1]]
                        arr[nx][ny] = [arr[x][y][0],arr[x][y][1]]
                        arr[x][y] = [tmp[0],tmp[1]]
                        break
                    else:
                        arr[x][y][1] = arr[x][y][1]+1 if arr[x][y][1] < 8 else 1
                return

def fishList(order):
    lst = []
    x,y = order
    dir = arr[x][y][1]
    cnt = 1
    while True:
        nx = x + cnt*dx[dir]
        ny = y + cnt*dy[dir]
        if 0 <= nx < 4 and 0 <= ny < 4:
            cnt += 1
            if arr[nx][ny][0] != 0:
                lst.append([nx,ny])
        else:
            break
    return lst

for i in range(4):
    tmp = list(map(int,sys.stdin.readline().split()))
    for j in range(4):
        arr[i][j] = [tmp[2*j], tmp[2*j+1]]

s = arr[0][0][0]
arr[0][0][0] = -1
moveOrder(s)
print(res)