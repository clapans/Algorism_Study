dx = [1,-1,0,0]
dy = [0,0,1,-1]

def move(x,y,visit):
    if len(visit) == 7:
        tmp = ''.join(visit)
        if tmp not in res:
            res.append(tmp)
    else:
        for t in range(4):
            new_x = x + dx[t]
            new_y = y + dy[t]
            if 0 <= new_x < 4 and 0 <= new_y < 4:
                visit.append(arr[new_x][new_y])
                move(new_x,new_y,visit)
                visit.pop()

for case in range(int(input())):
    arr = []
    for t in range(4):
        arr.append(list(input().split()))
    res = []
    for i in range(4):
        for j in range(4):
            move(i,j,[arr[i][j]])
    
    print(f'#{case+1} {len(res)}')