import sys

sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
tree = [[] for _ in range(n)]
visit = [0]*n

def dfs(x,cnt):
    if cnt == 5:
        print(1)
        quit()
    for t in tree[x]:
        if visit[t] == 0:
            visit[t] = 1
            dfs(t,cnt+1)
            visit[t] = 0
        
for _ in range(m):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(n):
    visit[i] = 1
    dfs(i,1)
    visit[i] = 0
    
print(0)