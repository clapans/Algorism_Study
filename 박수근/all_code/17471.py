import sys
from collections import deque

def bfs(red,blue):
    queue.append(red[0])
    visit = [0]*n
    while queue:
        tmp = queue.popleft()
        visit[tmp] = 1
        for i in arr[tmp]:
            if visit[i] == 0 and i in red:
                queue.append(i)
    for i in red:
        if visit[i] == 0:
            return int(1e9)
    visit = [0]*n
    queue.append(blue[0])
    while queue:
        tmp = queue.popleft()
        visit[tmp] = 1
        for i in arr[tmp]:
            if visit[i] == 0 and i in red:
                queue.append(i)
    for i in red:
        if visit[i] == 0:
            return int(1e9)
    red_sum = 0
    blue_sum = 0
    for i in range(n):
        if i in red:
            red_sum += population[i]
        else:
            blue_sum += population[i]
    return abs(red_sum - blue_sum)

def combi(x):
    global res
    if x == n:
        if len(red) < n and len(blue) < n:
            res = min(res,bfs(red,blue))
    else:
        red.append(x)
        combi(x+1)
        red.pop()
        blue.append(x)
        combi(x+1)
        blue.pop()

n = int(sys.stdin.readline())
population = list(map(int,sys.stdin.readline().split()))
red,blue = [],[]
arr = []
queue = deque([])
res = int(1e9)

for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    arr.append(list(map(lambda x : x-1,tmp[1:])))

combi(0)
if res == int(1e9):
    print(-1)
else:
    print(res)