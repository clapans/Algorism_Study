import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
arr = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
dp = [[int(1e9)]*(n*m) for _ in range(n*m)]

for _ in range(n):
    arr.append(list(sys.stdin.readline()))

def bfs(start):
    queue = deque([start])
    visit = [[0]*m for _ in range(n)]
    visit[start[0]][start[1]] = 1
    maxCnt = 0
    while queue:
        x,y = queue.popleft()
        maxCnt = max(maxCnt,visit[x][y])
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == "L" and visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                queue.append([nx,ny])
    
    return maxCnt

res = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            res = max(res,bfs([i,j]))

print(res - 1)