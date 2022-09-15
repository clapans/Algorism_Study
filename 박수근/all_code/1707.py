from collections import deque

n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    tree = [[] for t in range(a+1)]
    visit = [0] * (a+1)
    for j in range(b):
        x,y = map(int,input().split())
        tree[x].append(y)
        tree[y].append(x)
    for j in range(1,a+1):
        if visit[j] == 0:
            visit[j] = 1
            queue = deque([j])
            while queue:
                tmp = queue.popleft()
                for k in tree[tmp]:
                    if visit[k] == 0:
                        visit[k] = -visit[tmp]
                        queue.append(k)
                    else:
                        if visit[tmp] == visit[k]:
                            visit[k] = 3
    if visit.count(3) == 0:
        print("YES")
    else:
        print("NO")