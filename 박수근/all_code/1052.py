import sys

n,k = map(int,sys.stdin.readline().split())

cnt = 0
jar = []
for i in str(bin(n))[::-1][:-2]:
    if i == '1':
        jar.append(cnt)
    cnt += 1
if len(jar) <= k:
    print(0)
else:
    print(2**(jar[-k]+1) - sum([2**t for t in jar[:len(jar)-k+1]]))