import sys
from collections import deque
import heapq

def bfs(start):
    global res,size,eat
    able = []
    limit = int(1e9)
    while queue:
        x,y,cnt = queue.popleft()
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and arr[nx][ny] <= size:
                if arr[nx][ny] != 0 and arr[nx][ny] < size and cnt < limit:
                    heapq.heappush(able,[nx,ny])
                    limit = cnt + 1
                visit[nx][ny] = 1
                queue.append([nx,ny,cnt + 1])
    if able:
        tmp = heapq.heappop(able)
        arr[tmp[0]][tmp[1]] = 0
        start = tmp
        eat += 1
        res += limit
        if eat == size:
            size += 1
            eat = 0
        return start
    return 1

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            start = [i,j]
            arr[i][j] = 0

dx = [-1,0,0,1]
dy = [0,-1,1,0]

eat = 0
size = 2
res = 0

while True:
    queue = deque([[*start,0]])
    visit = [[0]*n for _ in range(n)]
    visit[start[0]][start[1]] = 1
    start = bfs(start)
    if start == 1:
        break

print(res)