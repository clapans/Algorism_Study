import sys

def dfs(x):
    if dp[x] > -1:
        return dp[x]
    tmp = 1
    for t in edges[x]:
        tmp *= dfs(t)
    if tmp:
        dp[x] = 0
    else:
        dp[x] = 1
    return dp[x]

nodes = int(sys.stdin.readline())
edges = [[] for _ in range(nodes+1)]

for t in range(nodes-1): 
    a,b = map(int,sys.stdin.readline().split())
    edges[a].append(b)

dp = [-1 for _ in range(nodes+1)]
dfs(1)
print(sum([t for t in dp[1:] if t != -1]))