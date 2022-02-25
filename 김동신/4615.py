T = int(input())

for t in range(T) :
    N, M = map(int,input().split())
    arr = [[0]*N for _ in range(N)]
    arr[(N-1)//2][(N-1)//2],arr[(N-1)//2+1][(N-1)//2+1] = 2,2
    arr[(N-1)//2+1][(N-1)//2],arr[(N-1)//2][(N-1)//2+1] = 1,1

    dx = [-1,1,0,0,1,1,-1,-1]
    dy = [0,0,-1,1,1,-1,1,-1]
    for _ in range(M) :
        *a,b =  map(int,input().split())
        x = a[1]-1
        y = a[0]-1

        arr[x][y] = b

        for k in range(8) :
            nx = x+dx[k]
            ny = y+dy[k]
            tmp = []
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 0 :
                continue

            while 0<=nx<N and 0<=ny<N and arr[nx][ny]!=b and arr[nx][ny]!=0 : # 여기에 0이 아닐 경우를 안넣어줘서 계속 19개만 맞음(30개중)
                tmp.append([nx,ny])
                nx += dx[k]
                ny += dy[k]

            if 0<=nx<N and 0<=ny<N and arr[nx][ny]==b:
                for ch1,ch2 in tmp :
                    arr[ch1][ch2] = b

    cnt_b = 0
    cnt_w = 0

    for nums in arr :
        for num in nums :
            if num == 1 :
                cnt_b += 1
            elif num == 2 :
                cnt_w += 1

    print(f"#{t+1} {cnt_b} {cnt_w}")