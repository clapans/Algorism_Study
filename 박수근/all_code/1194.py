import sys

m,n = map(int,sys.stdin.readline().split())
arr = []
bag = []
m_ = int(1e9)
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

def dfs(x,y,visit):
    if [x,y] == o_pos:
        return 0
    if dp[x][y][visit] != m_:
        return dp[x][y][visit]
    for t in range(4):
        nw_x = x + dx[t]
        nw_y = y + dy[t]
        if 0 <= nw_x < m and 0 <= nw_y < n and not arr[nw_x][nw_y] == '#':
            if arr[nw_x][nw_y].isupper():
                if arr[nw_x][nw_y].lower() in bag:
                    pass
                else:
                    continue
            dp[x][y][visit] = min(dp[x][y][visit],dfs(nw_x,nw_y,visit | (1 << nw_x*n+nw_y)))
    return dp[x][y][visit] + 1

dp = [[[m_]*(1 << m*n) for i in range(m)] for j in range(n)]

print(dfs(z_pos[0],z_pos[1],0 & (1 << z_pos[0]*n+z_pos[1])))