from pprint import pprint

def connect_line(xy) :
    global arr
    global loc_1
    global core

    for loc in range(len(loc_1)) :
        nx,ny=loc
        for k in range(4):
            tmp = [(0, 0)]
            nx += dx[k]
            ny += dy[k]
            while arr[nx][ny] == 0 :
                nx += dx[k]
                ny += dy[k]
                tmp.append((nx, ny))
            if arr[nx][ny] == 9:
                for cx, cy in tmp:
                    arr[cx][cy] = 2
                xy+=1
                core += 1
                connect_line(xy)
    else :
        line = 0
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if arr[i][j] == 2:
                    line += 1
        stack.append([core, line])
        for cx, cy in tmp:
            arr[cx][cy] = 0


T = int(input())
N = int(input())
arr = [[9]*(N+2)]
arr += [[9]+list(map(int,input().split()))+[9] for _ in range(N)]
arr.append([9]*(N+2))
pprint(arr)
stack = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

loc_1 = []

for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == 1 :
            loc_1.append([i,j])

core=0
connect_line(0)
pprint(arr)
print(stack)







