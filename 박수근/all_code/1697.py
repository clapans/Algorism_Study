import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())

s = deque([[n,0]])
visit = [0] * (100001)

while s:
    node = s.popleft()
    x = node[0]
    cnt = node[1]
    if x == k:
        print(cnt)
        break
    visit[x] = 1
    if 2*x <= 100000 and visit[2*x] == 0:
        s.append([2*x,cnt+1])
    if x + 1 <= 100000 and visit[x+1] == 0: 
        s.append([x+1,cnt+1])
    if 0 <= x - 1 and visit[x-1] == 0:    
        s.append([x-1,cnt+1])