import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def comb(x):
    global result
    if len(combi) == m:
        result = min(result,bfs(combi))
    else:
        if x < len(virus):
            combi.append(virus[x])
            comb(x+1)
            combi.pop()
            comb(x+1)

def bfs(lst):
    res = 0
    visit = [[int(1e9)]*n for _ in range(n)]
    queue = deque([])
    for t in lst:
        queue.append(t+[0])
        visit[t[0]][t[1]] = 0

    while queue:
        tmp = queue.popleft()
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] > tmp[2]+1:
                if arr[nx][ny] != 1:
                    visit[nx][ny] = tmp[2] + 1
                    queue.append([nx,ny,tmp[2]+1])
    
    for i in range(n):
        for j in range(n):
            if visit[i][j] == int(1e9):
                if arr[i][j] != 1:
                    return int(1e9)
            else:
                if arr[i][j] != 2:
                    res = max(res,visit[i][j])
    return res

n,m = map(int,sys.stdin.readline().split())
arr = []
virus = []
result = int(1e9)

for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            virus.append([i,j])

combi = []
comb(0)
if result == int(1e9):
    print(-1)
else:
    print(result)