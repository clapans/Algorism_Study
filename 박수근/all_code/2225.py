n,k = map(int,input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
dp[0] = [1] * (k+1)

def dfs(x,cnt):
    if dp[x][cnt]:
        return dp[x][cnt]
    if cnt == 1:
        dp[x][cnt] = dp[0][0]
    else:
        for i in range(x+1):
            dp[x][cnt] += dfs(i,cnt-1)  
        dp[x][cnt] = dp[x][cnt] % 1000000000
    return dp[x][cnt]

print(dfs(n,k))