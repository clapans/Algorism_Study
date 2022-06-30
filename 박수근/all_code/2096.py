import sys

n = int(sys.stdin.readline())
arr = []
dp = [[[0,int(1e9)] for i in range(3)] for j in range(2)]

def updateSum(j,dist,arr):
    dp[1][j+dist][0] = max(dp[1][j+dist][0], dp[0][j][0] + arr[j+dist])
    dp[1][j+dist][1] = min(dp[1][j+dist][1], dp[0][j][1] + arr[j+dist])

def transferDp():
    for i in range(3):
        dp[0][i] = dp[1][i]
        dp[1][i] = [0,int(1e9)]

tmp = list(map(int,sys.stdin.readline().split()))
for i in range(3):
    dp[0][i][0] = tmp[i]
    dp[0][i][1] = tmp[i]

for i in range(n-1):
    arr = list(map(int,sys.stdin.readline().split()))
    for j in range(3):
        if j > 0:
            updateSum(j,-1,arr)
        if j < 2:
            updateSum(j,1,arr)
        updateSum(j,0,arr)
    transferDp()

max_,min_ = 0,int(1e9)
for t in dp[0]:
    max_ = max(max_,t[0])
    min_ = min(min_,t[1])

print(max_,min_,sep=" ")