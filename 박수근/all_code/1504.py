import sys
import heapq

n,e = map(int,sys.stdin.readline().split())
arr = [[] for _ in range(n)]

for _ in range(e):
    s,e,cost = map(int,sys.stdin.readline().split())
    arr[s-1].append([cost,e-1])
    arr[e-1].append([cost,s-1])

v1,v2 = map(int,sys.stdin.readline().split())

def dijkstra(start,end):
    queue = [[0,start]]
    dp = [int(1e9)]*n
    dp[start] = 0
    while queue:
        cost,node = heapq.heappop(queue)
        if dp[node] < cost:
            continue
        for t in arr[node]:
            if dp[t[1]] > cost + t[0]:
                dp[t[1]] = cost + t[0]
                heapq.heappush(queue,[dp[t[1]],t[1]])
    return dp[end]

res = dijkstra(0,v1-1) + dijkstra(v1-1,v2-1) + dijkstra(v2-1,n-1)
res = min(res,dijkstra(0,v2-1) + dijkstra(v2-1,v1-1) + dijkstra(v1-1,n-1))

if res >= int(1e9):
    print(-1)
else:
    print(res)