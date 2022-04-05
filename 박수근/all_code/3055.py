import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(water,gos):
    time = 0
    while True:
        water_tmp = []
        gos_tmp = []
        while water:
            tmp = water.pop()
            for i in range(4):
                nx = tmp[0] + dx[i]
                ny = tmp[1] + dy[i]
                if 0 <= nx < r and 0 <= ny < c and visit[nx][ny] == 0 and arr[nx][ny] == '.':
                    visit[nx][ny] = 1
                    water_tmp.append([nx,ny])
        while gos:
            tmp = gos.pop()
            for i in range(4):
                nx = tmp[0] + dx[i]
                ny = tmp[1] + dy[i]
                if 0 <= nx < r and 0 <= ny < c and visit[nx][ny] == 0:
                    if arr[nx][ny] == '.':
                        visit[nx][ny] = 1
                        gos_tmp.append([nx,ny])
                    elif arr[nx][ny] == 'D':
                        print(time+1)
                        return
        time += 1
        water = water_tmp[:]
        gos = gos_tmp[:]
        if not gos:
            print('KAKTUS')
            return

water = []
gos = []
r,c = map(int,sys.stdin.readline().split())
arr = []
for _ in range(r):
    arr.append(list(input()))

visit = [[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if arr[i][j] == '*':
            water.append([i,j])
        elif arr[i][j] == 'S':
            gos.append([i,j])

bfs(water,gos)