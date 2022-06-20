import sys

sys.setrecursionlimit(10**6)
n,m = map(int,sys.stdin.readline().split())
parent = [t for t in range(n+1)]

def find(x):
    if x != parent[x]:
        tmp = find(parent[x])
        parent[x] = tmp
        return tmp
    return x

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[x] = y

def isCheck(x,y):
    if find(x) == find(y):
        return "YES"
    return "NO"

for _ in range(m):
    cal,a,b = map(int,sys.stdin.readline().split())
    if cal == 0:
        union(a,b)
    else:
        print(isCheck(a,b))