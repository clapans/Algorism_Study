dx = [-1,1,0,0]
dy = [0,0,-1,1]

block_dic = {1 : (1,3,0,2), 2 : (3,0,1,2), 3 : (2,0,3,1),
             4 : (1,2,3,0), 5 : (1,0,3,2)}

wall = {0: 1, 1: 0, 2: 3, 3: 2}

def pin_ball(x,y,dir,res):
    while True:
        x += dx[dir]
        y += dy[dir]
        if 0 <= x < n and 0 <= y < n:
            if len(visit) == 1 or visit[-2] != [x,y]:
                visit.append([x,y])
                if arr[x][y] == -1:
                    break
                elif 1 <= arr[x][y] <= 5:
                    dir = block_dic[arr[x][y]][dir]
                    res += 1
                elif 6 <= arr[x][y]:
                    for t in worm_hall[arr[x][y]]:
                        if t != [x,y]:
                            tmp = t
                    x,y = tmp
            else:
                res = 2*(res-1)+1
                break
        else:
            res = 2*res+1
            break
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
                for t in range(4):
                    visit = [[i,j]]
                    tmp = pin_ball(i,j,t,0)
                    res = max(res,tmp)

    print(f'#{case+1} {res}')