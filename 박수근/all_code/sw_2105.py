dx = [1,1]
dy = [1,-1]
r_dx = [-1,-1]
r_dy = [-1,1]

def dfs(x,y,val,dir,rotate):
    global res
    for t in range(2):
        if rotate == 0 or t == 1:
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] not in val:
                val.append(arr[nx][ny])
                dir.append(t)
                dfs(nx,ny,val,dir,max(rotate,t))
                dir.pop()
                val.pop()
    if 0 in dir and 1 in dir:
        for t in dir:
            x += r_dx[t]
            y += r_dy[t]
            if 0 <= x < n and 0 <= y < n and arr[x][y] not in val:
                val.append(arr[x][y])
            else:
                return 0
        res = max(res,len(val))
        
for case in range(int(input())):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    
    res = -1
    for i in range(n):
        for j in range(n):
            sx,sy = i,j
            dfs(i,j,[],[],0)
    print(f'#{case+1} {res}')    
