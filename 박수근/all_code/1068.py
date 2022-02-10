import sys

n = int(sys.stdin.readline())
tree = [[] for t in range(n)]
save_lst = list(map(int,sys.stdin.readline().split()))
for ix,t in enumerate(save_lst):
    if t > -1:
        tree[t].append(ix)

def dfs(x):
    global res
    ch = 0
    for t in tree[x]:
        if visit[t] == 0:
            visit[t] = 1
            dfs(t)
            visit[t] = 0
            ch = 1
    if ch == 0:
        res -= 1

res = tree.count([])
start = int(sys.stdin.readline())
visit = [0] * n
visit[start] = 1
dfs(start)
if len(tree[save_lst[start]]) == 1:
    res += 1
print(res)
