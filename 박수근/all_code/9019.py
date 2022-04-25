import sys
from collections import deque

def d(num):
    return 2*num % 10000

def s(num):
    return num-1 if num > 0 else 9999

def l(num):
    return 10*(num%1000) + num//1000

def r(num):
    return 1000*(num%10) + num//10

for _ in range(int(sys.stdin.readline())):
    a,b= map(int,sys.stdin.readline().split())
    visit = [0]*10000
    queue = deque([[a,""]])
    while queue:
        n = queue.popleft()
        if n[0] == b:
            print(n[1])
            break
        for t in [[d,"D"],[s,"S"],[l,"L"],[r,"R"]]:
            tmp = t[0](n[0])
            if visit[tmp] == 0:
                visit[tmp] = 1
                queue.append([tmp,n[1]+t[1]])