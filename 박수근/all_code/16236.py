import sys
from collections import deque
from pprint import pprint

def bfs(start):
    global res
    while queue:
        x,y,cnt = queue.popleft()
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and arr[nx][ny] <= arr[start[0]][start[1]]:
                if [nx,ny] in fishes and arr[nx][ny] < arr[start[0]][start[1]]:
                    eat.append([nx,ny])
                    fishes.remove([nx,ny])
                    arr[nx][ny] = arr[start[0]][start[1]]
                    arr[start[0]][start[1]] = 0
                    start = [nx,ny]
                    res += cnt + 1
                    return start
                visit[nx][ny] = 1
                queue.append([nx,ny,cnt + 1])
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
            arr[i][j] = 2
        elif arr[i][j] > 0:
            fishes.append([i,j])

dx = [-1,0,0,1]
dy = [0,-1,1,0]

eat = []
res = 0

while True:
    queue = deque([[*start,0]])
    visit = [[0]*n for _ in range(n)]
    visit[start[0]][start[1]] = 1
    start = bfs(start)
    if start == 1:
        break
    if len(eat) == arr[start[0]][start[1]]:
        arr[start[0]][start[1]] += 1
        eat = [] 

print(res)