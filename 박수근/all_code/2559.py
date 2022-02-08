import sys

n,k = map(int,sys.stdin.readline().split())
tempor = list(map(int,sys.stdin.readline().split()))
dp = [0] * (n-k+1)
dp[0] = sum(tempor[:k])

for i in range(1,n-k+1):
    dp[i] = dp[i-1] - tempor[i-1] + tempor[i+k-1]

print(max(dp))