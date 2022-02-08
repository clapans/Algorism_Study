import sys
from collections import deque

n = int(sys.stdin.readline())
friends = [[] for t in range(n)]

for i in range(n):
    s = list(sys.stdin.readline())
    for t in range(n):
        if s[t] == 'Y':
            friends[i].append(t)

res = 0

for i in range(n):
    visit = [0] * n
    visit[i] = 1
    queue = deque([[i,0]])
    while queue:
        tmp = queue.popleft()
        if tmp[1] == 2:
            break
        for t in friends[tmp[0]]:
            visit[t] = 1
            queue.append([t,tmp[1]+1])
    res = max(res,sum(visit)-1)

print(res)