import sys

n = int(sys.stdin.readline())
'''
arr = {}

for t in range(n):
    x,y,w,h = map(int,sys.stdin.readline().split())
    for i in range(x,x+w):
        for j in range(y,y+h):
            arr[(i,j)] = t

for t in range(n):
    print(list(arr.values()).count(t))
'''

arr = [[-1]*1001 for t in range(1001)]
res = [0] * n

for t in range(n):
    x,y,w,h = map(int,sys.stdin.readline().split())
    for i in range(x,x+w):
        for j in range(y,y+h):
            arr[i][j] = t

for i in range(1001):
    for j in range(1001):
        if arr[i][j] > -1:
            res[arr[i][j]] += 1

for t in range(n):
    print(res[t])