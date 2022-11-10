import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

trip = list(map(int,sys.stdin.readline().split()))

parent = [t for t in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        if x < y:
            parent[y] = x
        else:
            parent[x] = y

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            union(i+1,j+1)

isCheck = 'YES'
setN = find(trip[0])

for t in trip[1:]:
    if find(t) != setN:
        isCheck = 'NO'
        break

print(isCheck)