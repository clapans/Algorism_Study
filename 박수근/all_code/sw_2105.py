dx = [1,1,-1,-1]
dy = [1,-1,-1,1]
 
def dfs(x,y,val,dir):
    global res
    if x == sx and y == sy and val:
        res = max(res,len(val))
    else:
        try:
            if dir[-1] < 3:
                case = [dir[-1],dir[-1]+1]
            else:
                case = [dir[-1]]
        except:
            case = [0]
        for t in case:
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] not in val:
                val.append(arr[nx][ny])
                dir.append(t)
                dfs(nx,ny,val,dir)
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
            dfs(i,j,[],[])
    print(f'#{case+1} {res}')
