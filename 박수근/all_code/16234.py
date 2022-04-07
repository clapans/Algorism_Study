import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
    global check
    queue = deque([[i,j]])
    union = [[i,j]]
    while queue:
        x,y = queue.popleft()
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                distance = abs(arr[x][y] - arr[nx][ny])
                if (l <= distance <= r):
                    check = 1
                    visit[nx][ny] = 1
                    queue.append([nx,ny])
                    union.append([nx,ny])

    avg = sum([arr[t[0]][t[1]] for t in union])//len(union)
    for t in union:
        arr[t[0]][t[1]] = avg

n,l,r = map(int,sys.stdin.readline().split())
arr = []

for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

cnt = 0

while True:
    check = 0
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                visit[i][j] = 1
                bfs(i,j)
    if not check:
        break
    cnt += 1

print(cnt)