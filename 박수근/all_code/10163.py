import sys

n = int(sys.stdin.readline())
arr = {}

for t in range(n):
    x,y,w,h = map(int,sys.stdin.readline().split())
    for i in range(x,x+w):
        for j in range(y,y+h):
            arr[(i,j)] = t

for t in range(n):
    print(list(arr.values()).count(t))