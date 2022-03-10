dx = [1,1,-1,-1]
dy = [1,-1,-1,1]
 
def dfs(x,y,val,dir):
    global res
    if x == sx and y == sy and val:
        res = max(res,len(val))
    else:
        if val and dir < 3:
            case = [dir,dir+1]
        else:
            case = [dir]
        for t in case:
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] not in val:
                val.append(arr[nx][ny])
                dfs(nx,ny,val,t)
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
            dfs(i,j,[],0)
    print(f'#{case+1} {res}')