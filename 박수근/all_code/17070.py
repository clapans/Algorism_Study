import sys

n = int(sys.stdin.readline())
arr = []
dx = [-1,0,-1]
dy = [0,-1,-1]

dir = {
    0 : [0,2],
    1 : [1,2],
    2 : [0,1,2],
}

for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

dp = [[[-1 for i in range(3)] for j in range(n)] for k in range(n)]

def isCheck(x,y,d):
    if arr[x][y] == 1:
        return False
    if d < 2:
        if arr[x + dx[d]][y + dy[d]] != 0:
            return False
    else:
        for t in dir[d]:
            nx = x + dx[t]
            ny = y + dy[t]
            if arr[nx][ny] == 1:
                return False
    return True

def dfs(x,y,d):
    if dp[x][y][d] != -1:
        return dp[x][y][d]
    dp[x][y][d] = 0
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < n and isCheck(x,y,d):
        for t in dir[d]:
            dp[x][y][d] += dfs(nx,ny,t)
    return dp[x][y][d]

dp[0][1][1] = 1
print(dfs(n-1,n-1,2) + dfs(n-1,n-1,1) + dfs(n-1,n-1,0))