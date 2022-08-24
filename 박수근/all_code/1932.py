n = int(input())
dp = []

for i in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1,n):
    dp[i][0] += dp[i-1][0]
    dp[i][-1] += dp[i-1][-1]
    for j in range(1,i):
        dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])

print(max(dp[-1]))