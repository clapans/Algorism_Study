import sys
from collections import deque

def drop():
    for y in range(6):
        new_cln = []
        for x in range(12):
            if arr[x][y] != '.':
                new_cln.append(arr[x][y])
        new_cln = ['.']*(12 - len(new_cln)) + new_cln
        for x in range(12):
            arr[x][y] = new_cln[x]

def puyo():
    chain = 0
    while True:
        isDuplicate = False
        for i in range(12):
            for j in range(6):
                if arr[i][j] != '.' and isExplode(i,j,arr[i][j]) and not isDuplicate:
                    chain += 1
                    isDuplicate = True
        if not isDuplicate:
            return chain
        drop()
            
def isExplode(x,y,color):
    queue = deque([[x,y]])
    cnt = 1
    visit = [[x,y]]
    while queue:
        x,y = queue.popleft()
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < 12 and 0 <= ny < 6 and [nx,ny] not in visit and arr[nx][ny] == color:
                cnt += 1
                visit.append([nx,ny])
                queue.append([nx,ny])
    if cnt >= 4:
        for x,y in visit:
            arr[x][y] = '.'
        return True
    return False
    
arr = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for _ in range(12):
    arr.append(list(sys.stdin.readline().strip()))

print(puyo())