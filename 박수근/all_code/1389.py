import sys

n,m = map(int,sys.stdin.readline().split())
dp = [[int(1e9)]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    dp[a][b] = 1
    dp[b][a] = 1

def mapFriend():
    for mid in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dp[i][j] = min(dp[i][j],dp[i][mid] + dp[mid][j])

def kevinNum(num):
    tmp = 0
    for i in range(1,n+1):
        if i != num:
            tmp += dp[num][i]
    return tmp

res = 0
min_ = int(1e9)
mapFriend()

for i in range(1,n+1):
    tmp = kevinNum(i)
    if tmp < min_:
        res = i
        min_ = tmp
print(res)