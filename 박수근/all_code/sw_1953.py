from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
control_dict = {1 : [0,1,2,3], 2 : [0,1], 3 : [2,3],
                4 : [1,2],     5 : [0,2], 6 : [0,3], 7 : [1,3]}
move_dict = {0 : 1, 1 : 0, 2 : 3, 3 : 2}

def bfs(start_x,start_y,start_cnt):
    queue = deque([[start_x,start_y,start_cnt]])
    while queue:
        x,y,cnt = queue.popleft()
        if cnt < l-1:
            for t in control_dict[arr[x][y]]:
                nx = x + dx[t]
                ny = y + dy[t]
                if 0 <= nx < n and 0 <= ny < m:
                    if visit[nx][ny] == 0 and arr[nx][ny] > 0 and move_dict[t] in control_dict[arr[nx][ny]]:
                        visit[nx][ny] = 1
                        queue.append([nx,ny,cnt+1])

for case in range(int(input())):
    n,m,r,c,l = map(int,input().split())
    arr = []
    for t in range(n):
        arr.append(list(map(int,input().split())))
    visit = [[0]*m for _ in range(n)]
    visit[r][c] = 1
    bfs(r,c,0)
    res = sum([sum(t) for t in visit])
    print(f'#{case+1} {res}')