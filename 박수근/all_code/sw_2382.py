dx = [1,-1,0,0]
dy = [0,0,-1,1]
dir_dict = {0: 1, 1: 0, 2: 3, 3: 2}

for case in range(int(input())):
    n,m,k = map(int,input().split())
    arr = []
    for _ in range(k):
        arr.append(list(map(int,input().split())))
    while True:
        for t in arr:
            nx = t[0] + dx[t]
            ny = t[1] + dy[t]
            nx,ny = min(n-1,nx),min(n-1,ny)
            nx,ny = max(0,nx),max(0,nx)
            if nx == 0 or nx == n-1 or ny == 0 or ny == n-1:
