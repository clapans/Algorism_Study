import sys

sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
visit = [[1]*n for t in range(n)]
res = 0

def dfs(x,y):
    if visit[x][y] != 1:
        return visit[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] < arr[x][y]:
            visit[x][y] = max(visit[x][y],dfs(nx,ny) + 1)
    return visit[x][y]

for i in range(n):
    for j in range(n):
            res = max(res,dfs(i,j))

print(res)
