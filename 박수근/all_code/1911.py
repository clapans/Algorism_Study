import sys
import heapq

n,l = map(int,sys.stdin.readline().split())
heap = []

for _ in range(n):
    s,e = map(int,sys.stdin.readline().split())
    heapq.heappush(heap,[s,e-1])

start = 0
cnt = 0
while heap:
    s,e = heapq.heappop(heap)
    if s < start:
        s = start
    tmp = (e - s)//l + 1
    start = s + l*tmp 
    cnt += tmp

print(cnt)