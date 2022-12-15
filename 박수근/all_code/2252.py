from collections import deque

n,m = map(int,input().split())

arr = [[] for _ in range(n+1)]
in_ = [0 for _ in range(n+1)]
            
for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    in_[b] += 1

queue = deque([])
for i in range(1,n+1):
    if in_[i] == 0:
        queue.append(i)
        print(i,end=' ')

while queue:
    node = queue.popleft()
    for t in arr[node]:
        if in_[t]:
            if in_[t] == 1:
                queue.append(t)
                print(t,end=' ')
            in_[t] -= 1