import sys

w,h = map(int,sys.stdin.readline().split())
arr = [-1] * (2*(w+h))
n = int(sys.stdin.readline())

for t in range(n+1):
    x,y = map(int,sys.stdin.readline().split())
    if x == 1:
        arr[y] = t
    elif x == 2:
        arr[2*w+h-y] = t
    elif x == 3:
        arr[-y] = t
    else:
        arr[w+y] = t
    
x = arr.index(n)
cnt = 1
res = 0

while cnt <= w+h:
    tmp = x+cnt if x+cnt < 2*(w+h) else (x+cnt) - 2*(w+h)
    if arr[x-cnt] > -1:
        res += cnt
        arr[x-cnt] = -1
    if arr[tmp] > -1:
        res += cnt
        arr[tmp] = -1
    cnt += 1

print(res)