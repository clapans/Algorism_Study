import sys
from collections import deque

n,q = map(int,sys.stdin.readline().split())
n = 2**n
arr = []

for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

mage = list(map(int,sys.stdin.readline().split()))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def rotate(x,y,level):
    new_arr = [[0]*level for _ in range(level)]
    for i in range(level):
        for j in range(level):
            new_arr[j][level-i-1] = arr[x+i][y+j]
    for i in range(x,x+level):
        for j in range(y,y+level):
            arr[i][j] = new_arr[i-x][j-y]

def seperate(level):
    level = 2**level
    for i in range(n//level):
        i = level*i
        for j in range(n//level):
            j = level*j
            rotate(i,j,level)

def isMelt(x,y):
    cnt = 0
    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > 0:
            cnt += 1
    if cnt > 2:
        return True
    return False

def melt():
    melted_area = []
    for i in range(n):
        for j in range(n):
            if not isMelt(i,j):
                melted_area.append([i,j])
    for t in melted_area:
        arr[t[0]][t[1]] = max(arr[t[0]][t[1]] - 1,0)

def bfs(x,y):
    queue = deque([[x,y]])
    visit[x][y] = 1
    size = 1
    while queue:
        x,y = queue.popleft()
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and arr[nx][ny] > 0:
                visit[nx][ny] = 1
                size += 1
                queue.append([nx,ny])
    return size


res = 0
sum_ = 0
visit = [[0]*n for _ in range(n)]

for level in mage:
    seperate(level)
    melt()

for i in range(n):
    for j in range(n):
        sum_ += arr[i][j]
        if arr[i][j] > 0 and visit[i][j] == 0:
            res = max(res,bfs(i,j))

print(sum_)
print(res)