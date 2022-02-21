import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split())
arr = []

for t in range(m):
    arr.append(list(input()))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

res = int(1e9)
visit = [[[0]*(1 << 6) for i in range(n)] for j in range(m)]
for i in range(m):
    for j in range(n):
        if arr[i][j] == '0':
            queue = deque([[i,j,0,0]])
            visit[i][j][0] = 1
            while queue:
                tmp = queue.popleft()
                for t in range(4):
                    nw_x = tmp[0] + dx[t]
                    nw_y = tmp[1] + dy[t]
                    if 0 <= nw_x < m and 0 <= nw_y < n and arr[nw_x][nw_y] != '#' and not visit[nw_x][nw_y][tmp[2]]:
                        if arr[nw_x][nw_y] == '1':
                            print(tmp[3]+1)
                            quit(0)
                        elif arr[nw_x][nw_y].islower():
                            visit[nw_x][nw_y][tmp[2]] = 1
                            queue.append([nw_x,nw_y,tmp[2] | (1 << ord(arr[nw_x][nw_y]) - 97),tmp[3]+1])
                        elif arr[nw_x][nw_y].isupper():
                            if tmp[2] & (1 << ord(arr[nw_x][nw_y]) - 65):
                                visit[nw_x][nw_y][tmp[2]] = 1
                                queue.append([nw_x,nw_y,tmp[2],tmp[3]+1])
                        else:
                            visit[nw_x][nw_y][tmp[2]] = 1
                            queue.append([nw_x,nw_y,tmp[2],tmp[3]+1])
            print(-1)