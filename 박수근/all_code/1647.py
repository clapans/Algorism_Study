import sys
    
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[x] = y
        return True
    return False

n,m = map(int,sys.stdin.readline().split())
parent = [t for t in range(n+1)]
streetList = []
res = 0
highestCost = 0

for _ in range(m):
    s,e,cost = map(int,sys.stdin.readline().split())
    streetList.append([s,e,cost])

streetList.sort(key=lambda x: x[2])
for s,e,cost in streetList:
    if union(s,e):
        highestCost = cost
        res += cost

print(res - highestCost)