import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

island = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    island[a].append([b,c])
    island[b].append([a,c])

start,end = map(int,sys.stdin.readline().split())
max_ = 0
for t in island[start] + island[end]:
    max_ = max(max_,t[1])

res = 0

def bfs(limit):
    queue = deque([start])
    visit = [0]*(n+1)
    while queue:
        node = queue.popleft()
        for t in island[node]:
            if t[1] >= limit and visit[t[0]] == 0:
                queue.append(t[0])
                visit[t[0]] = 1
    return visit[end]

def binarySearch(s,e):
    global res
    if s <= e:
        mid = (s + e) // 2
        if bfs(mid):
            res = max(res,mid)
            binarySearch(mid + 1, e)
        else:
            binarySearch(s, mid - 1)

binarySearch(0,max_)
print(res)