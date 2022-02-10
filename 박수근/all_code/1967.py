import sys

sys.setrecursionlimit(10**6)
node = int(sys.stdin.readline())
trie = [[] for t in range(node+1)]

for t in range(node-1):
    a,b,c = map(int,sys.stdin.readline().split())
    trie[a].append([b,c])
    trie[b].append([a,c])

def dfs(x,val):
    global res,ix
    ch = 0
    for t in trie[x]:
         if visit[t[0]] == 0:
            visit[t[0]] = 1
            ch = 1
            dfs(t[0],val+t[1])
            visit[t[0]] = 0
    if ch == 0:
        if val > res:
            res = val
            ix = x

res,ix = 0,0
for t in range(1,node+1):
    if len(trie[t]) == 1:
        visit = [0] * (node+1)
        visit[t] = 1
        dfs(t,0)
        break

visit = [0] * (node+1)
visit[ix] = 1
dfs(ix,0)

print(res)