import sys

def flatten(x,y,num):
    if arr[x][y] < num:
        return num - arr[x][y]
    return 2 * (arr[x][y] - num)

def checkBlockCount(num):
    s = b
    for i in range(n):
        for j in range(m):
            s += arr[i][j] - num
    return s

n,m,b = map(int,sys.stdin.readline().split())
arr = []
max_ = 0
min_ = int(1e9)
res = int(1e9)

for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    max_ = max(max_,max(tmp))
    min_ = min(min_,min(tmp))
    arr.append(tmp)

for t in range(min_,max_+1):
    if checkBlockCount(t) >= 0:
        spend = 0 
        for i in range(n):
            for j in range(m):
                spend += flatten(i,j,t)
        if spend < res:
            res = spend
            height = t
        elif spend == res:
            height = max(height,t)

print(res,height,sep=" ")