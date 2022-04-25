import sys
from collections import deque

k = int(sys.stdin.readline())
w,h = map(int,sys.stdin.readline().split())
arr = []
dx = [1,-1,0,0,1,-1,2,-2,2,-2,1,-1]
dy = [0,0,1,-1,-2,-2,-1,-1,1,1,2,2]

for _ in range(h):
    arr.append(list(map(int,sys.stdin.readline().split())))

visit = [[[int(1e9)]*(k+1) for i in range(w)] for j in range(h)]
for t in range(k+1):
    visit[0][0][t] = 0

queue = deque([[0,0,0]])
while queue:
    tmp = queue.popleft()
    for t in range(12):
        nx = tmp[0] + dx[t]
        ny = tmp[1] + dy[t]
        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 0:
            if t > 3:
                if tmp[2] < k and visit[nx][ny][tmp[2]+1] > visit[tmp[0]][tmp[1]][tmp[2]] + 1:
                    visit[nx][ny][tmp[2]+1] = visit[tmp[0]][tmp[1]][tmp[2]] + 1
                    queue.append([nx,ny,tmp[2]+1])
            else:
                if visit[nx][ny][tmp[2]] > visit[tmp[0]][tmp[1]][tmp[2]] + 1:
                    visit[nx][ny][tmp[2]] = visit[tmp[0]][tmp[1]][tmp[2]] + 1
                    queue.append([nx,ny,tmp[2]])

if min(visit[-1][-1]) == int(1e9):
    print(-1)
else:
    print(min(visit[-1][-1]))