dx = [1,-1,0,0]
dy = [0,0,1,-1]

def mareummo(lst):
    cnt = 1
    sum_ = arr[i][j]
    res = 0
    if sum_ * m >= cnt**2 - (cnt-1)**2:
        res = max(res,sum_)
    cnt += 1
    while True:
        tmp = []
        for v in lst:
            for t in range(4):
                nx = v[0] + dx[t]
                ny = v[1] + dy[t]
                if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    if arr[nx][ny]:
                        sum_ += 1
                    tmp.append([nx,ny])
        if not tmp:
            break
        lst = tmp[:]
        if sum_ * m >= cnt**2 + (cnt-1)**2:
            res = max(res,sum_)
        cnt += 1
        
    return res

for case in range(int(input())):
    n,m = map(int,input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    res = 0
    for i in range(n):
        for j in range(n):
            visit = [[0]*n for _ in range(n)]
            visit[i][j] = 1
            res = max(res,mareummo([[i,j]]))
    
    print(f'#{case+1} {res}')