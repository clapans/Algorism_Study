import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
dp = [[0,0] for _ in range(n)]
dp[0] = [1,1]

for t in range(1,n):
    if arr[t] > arr[t-1]:
        dp[t][0] = dp[t-1][0] + 1
        dp[t][1] = 1
    elif arr[t] == arr[t-1]:
        dp[t][0] = dp[t-1][0] + 1
        dp[t][1] = dp[t-1][1] + 1
    else:
        dp[t][1] = dp[t-1][1] + 1
        dp[t][0] = 1

print(max([max(t) for t in dp]))