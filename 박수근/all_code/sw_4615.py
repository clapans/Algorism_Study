dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,-1,1,1,-1]

def osello(x,y,color):
    arr[x][y] = color
    for t in range(8):
        tmp = []
        cnt = 1
        while True:
            nx = x + cnt*dx[t]
            ny = y + cnt*dy[t]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny]:
                if arr[nx][ny] != color:
                    tmp.append([nx,ny])
                else:
                    for v in tmp:
                        arr[v[0]][v[1]] = color
                    break
            else:
                break
            cnt += 1

for case in range(int(input())):
    n,m = map(int,input().split())
    arr = [[False]*n for _ in range(n)]
    arr[n//2-1][n//2-1],arr[n//2][n//2] = 2,2
    arr[n//2-1][n//2],arr[n//2][n//2-1] = 1,1
    for t in range(m):
        a,b,c = map(int,input().split())
        osello(a-1,b-1,c)
    b_cnt,w_cnt = 0,0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                b_cnt += 1
            elif arr[i][j] == 2:
                w_cnt += 1
    print(f'#{case+1} {b_cnt} {w_cnt}')