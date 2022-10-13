import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
line = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,cost = map(int,sys.stdin.readline().split())
    line[s].append([cost,e])

sNode,eNode = map(int,sys.stdin.readline().split())

dp = [int(1e9)]*(n+1)

def dijkstra():
    queue = [[0,sNode]]
    while queue:
        cost,desti = heapq.heappop(queue)
        if cost > dp[desti]:
            continue
        for node in line[desti]:
            if cost + node[0] < dp[node[1]]:
                heapq.heappush(queue,[cost + node[0],node[1]])
                dp[node[1]] = cost + node[0]

dijkstra()
print(dp[eNode])