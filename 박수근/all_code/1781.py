import heapq

n = int(input())
arr = []
queue = []

for _ in range(n):
    a,b = map(int,input().split())
    heapq.heappush(arr,[a,b])

while arr:
    el = heapq.heappop(arr)
    heapq.heappush(queue,el[1])
    if el[0] < len(queue):
        heapq.heappop(queue)

print(sum(queue))