import sys
from collections import deque

n = int(sys.stdin.readline())
arr = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(n):
    arr.append(sys.stdin.readline().split())

visit = [[0]*n for _ in range(n)]

def bfs(queue):
    candidate = []
    while queue:
        x,y = queue.popleft()
        if isBorder(x,y):
            candidate.append([x,y])
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == "1" and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                queue.append([nx,ny])
    return candidate

def isBorder(x,y):
    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == "0":
            return True
    return False

def distance(x,y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def compare(x,y):
    bridge = int(1e9)
    for i in x:
        for j in y:
            bridge = min(bridge,distance(i,j)-1)
    return bridge

res = int(1e9)

border = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == "1" and visit[i][j] == 0:
            queue = deque([[i,j]])
            visit[i][j] = 1
            border.append(bfs(queue))

for i in range(len(border)):
    for j in range(i+1,len(border)):
        res = min(res,compare(border[i],border[j]))

print(res)