import sys
from collections import deque

n = int(sys.stdin.readline())

def divideThree(num):
    return num * 3

def divideTwo(num):
    return num * 2

def subtract(num):
    return num + 1

visit = [[] for _ in range(n+1)]
queue = deque([1])
visit[1] = [1]
while queue:
    num = queue.popleft()
    if n == num:
        break
    for t in [divideThree,divideTwo,subtract]:
        tmp = t(num)
        if num != tmp and tmp <= n and not visit[tmp]:
            visit[tmp] = [tmp] + visit[num]
            queue.append(tmp)

print(len(visit[n]) - 1)
print(*visit[n])