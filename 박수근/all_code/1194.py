import sys

m,n = map(int,sys.stdin.readline().split())
arr = []

for t in range(m):
    arr.append(list(input()))

for i in range(m):
    for j in range(n):
        if arr[i][j] == '0':
            z_pos = [i,j]
        if arr[i][j] == '1':
            o_pos = [i,j]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
dic_ = {'A': 1, 'B': 2, 'C': 4, 'D': 8, 'E': 16, 'F': 32}

def dfs(x,y,b,cnt):
    global res
    if [x,y] == o_pos:
        res = min(res,cnt)
    for t in range(4):
        nw_x = x + dx[t]
        nw_y = y + dy[t]
        if 0 <= nw_x < m and 0 <= nw_y < n and arr[nw_x][nw_y] != '#' and not visit[nw_x][nw_y][b]:
            if arr[nw_x][nw_y].islower():
                b = b | (1 << dic_[arr[nw_x][nw_y].upper()])
            elif arr[nw_x][nw_y].isupper():
                if b & (1 << dic_[arr[nw_x][nw_y]]):
                    pass
                else:
                    continue
            visit[nw_x][nw_y][b] = 1
            dfs(nw_x,nw_y,b,cnt+1)
            visit[nw_x][nw_y][b] = 0

res = int(1e9)
visit = [[[0]*(1 << 6) for i in range(m)] for j in range(n)]
dfs(z_pos[0],z_pos[1],0,0)
print(res)