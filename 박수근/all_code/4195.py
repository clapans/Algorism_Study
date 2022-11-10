import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        if x < y:
            parent[x] = y
            return updateUnionCnt(y,unionCnt[x])
        else:
            parent[y] = x
            return updateUnionCnt(x,unionCnt[y])
    return unionCnt[x]

def insert(x):
    try:
        parent[x]            
    except:
        parent[x] = x
        unionCnt[x] = 1

def updateUnionCnt(x,extra):
    unionCnt[x] += extra
    return unionCnt[x]

for case in range(int(sys.stdin.readline())):
    f = int(sys.stdin.readline())
    parent = {}
    unionCnt = {}
    for _ in range(f):
        x,y = sys.stdin.readline().split()
        insert(x)
        insert(y)
        print(union(x,y))