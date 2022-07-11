import sys

def distance():
    for middle in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dp[i][j] = min(dp[i][j],dp[i][middle] + dp[middle][j])
                if i == j and dp[i][j] < 0:
                    return "YES"
    return "NO"

for case in range(int(sys.stdin.readline())):
    n,m,w = map(int,sys.stdin.readline().split())
    dp = [[int(1e9)]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        s,e,t = map(int,sys.stdin.readline().split())
        dp[s][e] = min(dp[s][e],t)
        dp[e][s] = min(dp[e][s],t)
    for _ in range(w):
        s,e,t = map(int,sys.stdin.readline().split())
        dp[s][e] = -t
    print(distance())
