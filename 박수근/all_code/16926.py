import sys
from collections import deque

def rotate(index):
    tmp = classify[index].popleft()
    classify[index].append(tmp)

def transfer(command):
    dir,index = 0,0
    x,y = 0,0
    visit = [[0]*m for _ in range(n)]
    visit[x][y] = 1
    cnt = 0

    while True:
        if command == "decode":
            classify[index].append(arr[x][y])
        else:
            arr[x][y] = classify[index].popleft()
        cnt += 1
        if cnt == n*m:
            break
        if not (0 <= x + dx[dir] < n and 0 <= y + dy[dir] < m and visit[x + dx[dir]][y + dy[dir]] == 0):
            if dir < 3:
                dir += 1
            else:
                dir = 0
                index += 1
        x += dx[dir]
        y += dy[dir]
        visit[x][y] = 1
        
n,m,r = map(int,sys.stdin.readline().split())
arr = []
classify = [deque([]) for _ in range(min(n,m) // 2)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for _ in range(n):
    arr.append(sys.stdin.readline().split())

transfer("decode")

for idx in range(min(n,m) // 2):
    for _ in range(r % len(classify[idx])):
        rotate(idx)

transfer("encode")

for i in range(n):
    for j in range(m):
        print(arr[i][j],end = ' ')
    print('')