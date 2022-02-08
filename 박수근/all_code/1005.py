import sys

def dfs(x):
    if dp[x] >= 0:
        return dp[x]
    tmp = 0
    for t in sequence[x]:
        tmp = max(tmp,dfs(t))
    dp[x] = tmp + spent[x]
    return dp[x]

sys.setrecursionlimit(10**6)
for case in range(int(sys.stdin.readline())):
    n,k = map(int,sys.stdin.readline().split())
    spent = [0] + list(map(int,sys.stdin.readline().split()))
    sequence = [[] for t in range(n+1)]
    dp = [-1] * (n+1)
    for i in range(k):
        a,b = map(int,sys.stdin.readline().split())
        sequence[b].append(a)
    num = int(sys.stdin.readline())
    print(dfs(num))