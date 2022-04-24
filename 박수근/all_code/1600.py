import sys
from collections import deque

k = int(sys.stdin.readline())
w,h = map(int,sys.stdin.readline().split())
arr = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
d_horse_x = [1,-1,2,-2,2,-2,1,-1]
d_horse_y = [-2,-2,-1,-1,1,1,2,2]

for _ in range(h):
    arr.append(list(map(int,sys.stdin.readline().split())))

visit = [[[int(1e9)]*k for i in range(w)] for j in range(h)]

queue = deque([[0,0]])
while queue:
    tmp = queue.popleft()
    for t in range(4):
        nx = tmp[0] + dx[t]
        ny = tmp[1] + dy[t]
        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 0:
            for v in range(k):
                if visit[nx][ny][v] > visit[tmp[0]][tmp[1]] + 1:


