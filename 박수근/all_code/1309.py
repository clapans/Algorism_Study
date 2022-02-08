import sys

dp = [[0,0,0,0] for t in range(int(sys.stdin.readline()))]

dp[0] = [1,1,1,3]

for i in range(1,len(dp)):
    dp[i][0] = dp[i-1][-1] 
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901
    dp[i][3] = (dp[i][0] + dp[i][1] + dp[i][2]) % 9901

print(dp[-1][-1])