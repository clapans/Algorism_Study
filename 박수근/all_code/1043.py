import sys

n,m = map(int,sys.stdin.readline().split())
known = [-2]*(n+1)

for t in list(map(int,sys.stdin.readline().split()))[1:]:
    known[t] = 0

participant = []

for _ in range(m):
    participant.append(list(map(int,sys.stdin.readline().split()))[1:])

res = 0

def dfs(v,cnt):
    global res
    if v == m:
        res = max(res,cnt)
    else:
        arr_save = [known[t] for t in participant[v]]
        group = parent(v)
        if 0 not in group:
            union(v,[-1]*len(participant[v]))
            dfs(v+1,cnt+1)
            union(v,arr_save)
        if -1 not in group:
            union(v,[0]*len(participant[v]))
            dfs(v+1,cnt)
            union(v,arr_save)

def parent(v):
    parent = []
    for t in participant[v]:
        if known[t] == 0 or known[t] == -1:
            parent.append(known[t])    
    return parent

def union(v,x):
    for t in range(len(participant[v])):
        known[participant[v][t]] = x[t]

dfs(0,0)

print(res)