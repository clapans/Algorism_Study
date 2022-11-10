import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
dic_ = {}
visit = [int(1e9)] * 101

for _ in range(n+m):
    x,y = map(int,sys.stdin.readline().split())
    dic_[x] = y

queue = deque([1])
visit[1] = 0

while queue:
    node = queue.popleft()
    if node == 100:
        break
    try:
        nnode = dic_[node]
        if visit[nnode] > visit[node]:
            visit[nnode] = visit[node]
            queue.append(nnode)
        continue
    except:
        pass
    for t in range(1,7):
        new = node + t
        if new <= 100 and visit[new] > visit[node] + 1:
            visit[new] = visit[node] + 1
            queue.append(new)

print(visit[100])