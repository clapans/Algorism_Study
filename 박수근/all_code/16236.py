import sys
from collections import deque
import heapq

def bfs(start):
    global res
    able = []
    limit = int(1e9)
    while queue:
        x,y,cnt = queue.popleft()
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and arr[nx][ny] <= size:
                if [nx,ny] in fishes and arr[nx][ny] < size and cnt < limit:
                    heapq.heappush(able,[nx,ny])
                    limit = cnt + 1
                visit[nx][ny] = 1
                queue.append([nx,ny,cnt + 1])
    if able:
        tmp = heapq.heappop(able)
        eat.append(tmp)
        fishes.remove(tmp)
        arr[tmp[0]][tmp[1]] = 9
        arr[start[0]][start[1]] = 0
        start = tmp
        res += limit
        return start
    return 1

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

fishes = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            start = [i,j]
        elif arr[i][j] > 0:
            fishes.append([i,j])

dx = [-1,0,0,1]
dy = [0,-1,1,0]

eat = []
size = 2
res = 0

while True:
    queue = deque([[*start,0]])
    visit = [[0]*n for _ in range(n)]
    visit[start[0]][start[1]] = 1
    start = bfs(start)
    if start == 1:
        break
    if len(eat) == size:
        size += 1
        eat = [] 

print(res)