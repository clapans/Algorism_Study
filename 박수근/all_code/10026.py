from collections import deque
import sys

n = int(sys.stdin.readline())
arr = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    tmp = input()
    arr.append(list(tmp))

cnt_a = 0
cnt_b = 0

def bfs(color):
    queue = deque([[i,j]])
    while queue:
        tmp = queue.popleft()
        for t in range(4):
            x = tmp[0] + dx[t]
            y = tmp[1] + dy[t]
            if 0 <= x < n and 0 <= y < n and arr[x][y] in color and visit[x][y] == 0:
                visit[x][y] = 1
                queue.append([x,y])

visit = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            visit[i][j] = 1
            cnt_a += 1
            color = [arr[i][j]]
            bfs(color)

visit = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            visit[i][j] = 1
            cnt_b += 1
            if arr[i][j] == 'G' or arr[i][j] == 'R':
                color = ['G','R']
            else:
                color = ['B'] 
            bfs(color)
            
print(cnt_a,cnt_b)