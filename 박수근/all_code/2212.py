import sys
import heapq

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensor = list(map(int,sys.stdin.readline().split()))

if k >= n:
    print(0)
    quit()
    
sensor.sort()
distance = []

for i in range(1,n):
    heapq.heappush(distance,-(sensor[i] - sensor[i - 1]))

for i in range(k-1):
    heapq.heappop(distance)

print(-sum(distance))