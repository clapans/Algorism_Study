import sys
import heapq

n,m,x = map(int,sys.stdin.readline().split())
arr = [[] for _ in range(n)]

for _ in range(m):
    start,end,cost = map(int,sys.stdin.readline().split())
    arr[start - 1].append([cost,end - 1])

def shortWay(start,end):
    queue = [[0,start]]
    dp = [int(1e9)]*n
    dp[start] = 0
    while queue:
        cost,node = heapq.heappop(queue)
        if node == end:
            break
        if dp[node] < cost:
            continue
        for t in arr[node]:
            if dp[t[1]] > t[0] + cost:
                dp[t[1]] = t[0] + cost
                heapq.heappush(queue,[dp[t[1]],t[1]])
    return dp[end]

res = 0

for i in range(n):
    res = max(res,shortWay(i,x-1) + shortWay(x-1,i))

print(res)