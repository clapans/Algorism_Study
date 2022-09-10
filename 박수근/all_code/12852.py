import sys

n = int(sys.stdin.readline())

def divideThree(num):
    if num % 3 == 0:
        return num // 3
    return num

def divideTwo(num):
    if num % 2 == 0:
        return num // 2
    return num

def subtract(num):
    return num - 1

def dfs(num):
    if num != 1:
        for t in [divideThree,divideTwo,subtract]:
            tmp = t(num)
            if num != tmp and dp[num] + 1 < dp[tmp]:
                dp[tmp] = dp[num] + 1
                dfs(tmp)

dp = [int(1e9)]*(n+1)
dp[n] = 0
dfs(n)
print(dp[1])