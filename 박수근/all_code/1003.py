import sys

case = int(sys.stdin.readline())
nums = []

for _ in range(case):
    nums.append(int(sys.stdin.readline()))

dp = [[0,0]]*(max(max(nums)+1,2))
dp[0] = [1,0]
dp[1] = [0,1]

def fibonacci(n):
    if dp[n] != [0,0]:
        return dp[n]
    dp[n] = concatArray(fibonacci(n-1),fibonacci(n-2))
    return dp[n]

def concatArray(a,b):
    return [a[0] + b[0], a[1] + b[1]]

for n in nums:
    print(*fibonacci(n))