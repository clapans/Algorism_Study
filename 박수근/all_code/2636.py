from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
    queue = deque([[i,j]])
    while queue:
        x,y = queue.popleft()
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < r and 0 <= ny < c and visit[nx][ny] == 0 and arr[nx][ny] == 0:
                visit[nx][ny] = 1
                queue.append([nx,ny])

def visit_check(x,y):
    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]
        if visit[nx][ny]:
            return True
    return False

r,c = map(int,input().split())
arr = []
for _ in range(r):
    arr.append(list(map(int,input().split())))

cnt,pre = 0,0

while True:
    visit = [[0]*c for _ in range(r)]
    bfs(0,0)
    disappear = []
    for i in range(1,r-1):
        for j in range(1,c-1):
            if arr[i][j] and visit_check(i,j):
                disappear.append([i,j])
    if not disappear:
        break
    for i in disappear:
        arr[i[0]][i[1]] = 0
    pre = len(disappear)
    cnt += 1

print(cnt)
print(pre)