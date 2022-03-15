import sys
import heapq

def dijkstra():
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        tmp = heapq.heappop(q)
        if distance[tmp[1]] < tmp[0]:
            continue
        for t in graph(tmp[1]):
            cost = tmp[0] + t[1]
            if cost < distance[t[0]]:
                distance[t[0]] = cost
                heapq.heappush(q,(distance[t[0]],t[0]))

v,e = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c, = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
distance = [int(1e9)] * (v+1)
