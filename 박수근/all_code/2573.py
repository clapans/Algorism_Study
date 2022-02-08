import sys
import copy
from collections import deque

a,b = map(int,sys.stdin.readline().split())
area = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(a):
    area.append(list(map(int,sys.stdin.readline().split())))

cnt = 0

while True:
    if sum(sum(t) for t in area) == 0:
        print(0)
        exit(0)
    visit = [[0]*b for t in range(a)]
    save = copy.deepcopy(area)
    ch = 0
    for i in range(a):
        for j in range(b):
            if area[i][j] != 0 and visit[i][j] == 0:
                if ch == 1:
                    print(cnt)
                    exit(0)
                queue = deque([[i,j]])
                visit[i][j] = 1
                while queue:
                    tmp = queue.popleft()
                    for t in range(4):
                        nx = tmp[0] + dx[t]
                        ny = tmp[1] + dy[t]
                        if 0 <= nx < a and 0 <= ny < b:
                            if save[nx][ny] == 0:
                                area[tmp[0]][tmp[1]] = max(area[tmp[0]][tmp[1]]-1,0)
                            else:
                                if visit[nx][ny] == 0:
                                    visit[nx][ny] = 1
                                    queue.append([nx,ny])
                ch = 1
    cnt += 1
                