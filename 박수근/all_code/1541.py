import sys

s = sys.stdin.readline().split('-')

for i in s:
    tmp = sum(list(map(int,i.split('+'))))
    try:
        res -= tmp
    except:
        res = tmp

print(res)