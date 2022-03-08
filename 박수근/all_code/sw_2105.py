dx = [1,-1,1,-1]
dy = [-1,1,1,-1]

def dfs(x,y,val,dir,tst):
    global res
    if x == sx and y == sy and val:
        res = max(res,len(val))
    else:
        try:
            case = [dir[-1]] + [v for v in range(4) if v not in dir and (dx[v] != -dx[dir[-1]] or dy[v] != -dy[dir[-1]])]
        except:
            case = [v for v in range(4)]
        for t in case:
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] not in val:
                val.append(arr[nx][ny])
                dir.append(t)
                tst.append([nx,ny])
                dfs(nx,ny,val,dir,tst)
                dir.pop()
                val.pop()

for case in range(int(input())):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    
    res = -1
    for i in range(n):
        for j in range(n):
            sx,sy = i,j
            dfs(i,j,[],[],[])
    print(f'#{case+1} {res}')    
