import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split())
arr = []
for _ in range(m):
    arr.append(list(map(int,sys.stdin.readline().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

t_cnt = 0
while True:
    visit = [[0]*n for _ in range(m)]
    ch = 1
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1 and visit[i][j] == 0:
                ch = 0
                queue = deque([[i,j]])
                while queue:
                    tmp = queue.popleft()
                    visit[tmp[0]][tmp[1]] = 1
                    cnt = 0
                    for t in range(4):
                        nx = tmp[0] + dx[t]
                        ny = tmp[1] + dy[t]
                        if 0 <= nx < m and 0 <= ny < n:
                            if visit[nx][ny] == 1 and arr[nx][ny] == 0:
                                cnt += 1
                            if visit[nx][ny] == 0 and arr[nx][ny] == 1:
                                queue.append([nx,ny])
                    if cnt > 1:
                        arr[tmp[0]][tmp[1]] = -1
    if ch:
        print(t_cnt)
        break
    for i in range(m):
        for j in range(n):
            if arr[i][j] == -1:
                arr[i][j] = 0
    t_cnt += 1