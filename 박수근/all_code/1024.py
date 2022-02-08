import sys

n,l = map(int,sys.stdin.readline().split())
lst = [-1]

while l <= 100:
    if l % 2 == 1:
        if n % l == 0 and n // l - l // 2 >= 0:
            lst = [t for t in range(n//l-l//2,n//l+l//2+1)]
            break
    else:
        if n % (l//2) == 0 and (n // (l//2)) % 2 == 1 and (n//(l//2))//2-(l//2-1) >= 0:
            lst = [t for t in range((n//(l//2))//2-(l//2-1),(n//(l//2))//2+l//2+1)]
            break
    l += 1

for i in lst:
    print(i,end=' ')

