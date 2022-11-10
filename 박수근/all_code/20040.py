import sys

n,m = map(int,sys.stdin.readline().split())

parents = [t for t in range(n)]
res = 0

def find(x):
    if x == parents[x]:
        return x
    else:
        y = find(parents[x])
        parents[x] = y
        return y

def union(x, y, time):
    global res
    x = find(x)
    y = find(y)
    if x != y:
        parents[max(x,y)] = min(x,y)
    else:
        if res == 0:
            res = time

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b, i + 1)

print(res)