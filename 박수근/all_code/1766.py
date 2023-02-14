import heapq

n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
degree = [0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    degree[b] += 1 
    heapq.heappush(arr[a],b)

queue = []

for i in range(1,n+1):
    if not degree[i]:
        heapq.heappush(queue,i)

while queue:
    node = heapq.heappop(queue)
    print(node,end=" ")
    while arr[node]:
        x = heapq.heappop(arr[node])
        degree[x] -= 1
        if not degree[x]:
            heapq.heappush(queue,x)