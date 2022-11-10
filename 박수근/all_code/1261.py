import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,sys.stdin.readline().split())
arr = []
for _ in range(m):
    arr.append(list(sys.stdin.readline().strip()))

visit = [[int(1e9)]*n for _ in range(m)]
queue = deque([[0,0]])
visit[0][0] = 0
while queue:
    x,y = queue.popleft()
    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]
        if 0 <= nx < m and 0 <= ny < n:
            if arr[nx][ny] == '0' and visit[nx][ny] > visit[x][y]:
                visit[nx][ny] = visit[x][y]
                queue.append([nx,ny]) 
            elif arr[nx][ny] == '1' and visit[nx][ny] > visit[x][y] + 1:
                visit[nx][ny] = visit[x][y] + 1
                queue.append([nx,ny])

print(visit[m-1][n-1])        