import sys

n = int(input())
s = list(map(int,sys.stdin.readline().split()))
s.sort()

cnt = 0
for i in s:
    if i <= cnt + 1:
        cnt += i
    else:
        break
print(cnt + 1)
