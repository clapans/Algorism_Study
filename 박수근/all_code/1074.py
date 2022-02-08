import sys

n,x,y = map(int,sys.stdin.readline().split())
cnt = 0
n = 2**n

while n > 1:
    if x < n//2 and y < n//2:
        pass
    elif x < n//2 and y >= n//2:
        cnt += (n**2)//4
        y -= n//2
    elif x >= n//2 and y < n//2:
        cnt += (n**2)//2
        x -= n//2
    else:
        cnt += 3*(n**2)//4
        x -= n//2
        y -= n//2
    n = n//2

print(cnt)



