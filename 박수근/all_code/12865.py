import sys

n,k = map(int,sys.stdin.readline().split())
bag = []

for _ in range(n):
    bag.append(list(map(int,sys.stdin.readline().split())))

bag.sort(key = lambda x: x[0])
dp = [0] * (max(k,bag[-1][0])+1)

for t in bag:
    case = [v for v in range(1,k+1) if dp[v]]
    tmp = []
    for v in case:
        try:
            tmp.append([v+t[0],max(dp[v+t[0]],dp[v]+t[1])])
        except:
            pass
    for v in tmp:
        dp[v[0]] = v[1]
    dp[t[0]] = max(dp[t[0]],t[1])

print(max(dp[:k+1]))