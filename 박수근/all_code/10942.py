import sys

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

dp = [[0]*n for _ in range(n)]
cnt = 0
while cnt < n:
    for i in range(n-cnt):
        j = i + cnt
        if nums[i] == nums[j]:
            if j - i > 1:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1
    cnt += 1

for _ in range(int(sys.stdin.readline())):
    s,e = map(int,sys.stdin.readline().split())
    print(dp[s-1][e-1])