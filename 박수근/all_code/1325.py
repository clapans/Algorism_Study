import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
hack = [[] for t in range(n+1)]
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    hack[b].append(a)

res = []
max_ = 0

for i in range(1,n+1):
    queue = deque([i])
    visit = [0]*(n+1)
    visit[i] = 1
    cnt = 1
    while queue:
        tmp = queue.popleft()
        for j in hack[tmp]:
            if visit[j] == 0:
                visit[j] = 1
                queue.append(j)
                cnt += 1
    if cnt > max_:
        res = [i]
        max_ = cnt
    elif cnt == max_:
        res.append(i)

print(*res)

