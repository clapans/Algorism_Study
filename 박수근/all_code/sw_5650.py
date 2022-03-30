dx = [-1,1,0,0]
dy = [0,0,-1,1]

block_dic = {1 : (1,3,0,2), 2 : (3,0,1,2), 3 : (2,0,3,1),
             4 : (1,2,3,0), 5 : (1,0,3,2)}

wall = {0: 1, 1: 0, 2: 3, 3: 2}

def pin_ball(x,y,dir,res,start):
    while True:
        if [x,y] == start and res != 0:
            break
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == -1:
                break
            elif 1 <= arr[nx][ny] <= 5:
                res += 1
                dir = block_dic[arr[nx][ny]][dir]
                x,y = nx,ny
            elif 6 <= arr[nx][ny]:
                for t in worm_hall[arr[nx][ny]]:
                    if t != [nx,ny]:
                        tmp = t
                x,y = tmp
            else:
                x,y = nx,ny
        else:
            dir = wall[dir]
            res += 1
            x,y = nx,ny
    return res
    
for case in range(int(input())):
    n = int(input())
    arr = []
    worm_hall = [[] for _ in range(11)]
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 6:
                worm_hall[arr[i][j]].append([i,j])
    
    res = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                start = [i,j]
                for t in range(4):
                    tmp = pin_ball(i,j,t,0,start)
                    if tmp:
                        res = max(res,tmp)

    print(f'#{case+1} {res}')