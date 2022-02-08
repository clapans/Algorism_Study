import sys
from collections import deque

m,n,h = map(int,sys.stdin.readline().split())
arr = []
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

for i in range(h):
    floor = []
    for j in range(n):
       floor.append(list(map(int,sys.stdin.readline().split()))) 
    arr.append(floor)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                queue = deque([[i,j,k,2]])
                while queue:
                    tmp = queue.popleft()
                    for t in range(6):
                        new_x = tmp[2] + dx[t]
                        new_y = tmp[1] + dy[t]
                        new_z = tmp[0] + dz[t]
                        if 0 <= new_x < m and 0 <= new_y < n and 0 <= new_z < h:
                            if arr[new_z][new_y][new_x] == 0 or arr[new_z][new_y][new_x] > tmp[3]:
                                queue.append([new_z,new_y,new_x,tmp[3]+1])
                                arr[new_z][new_y][new_x] = tmp[3]

def func():
    res = 0
    for i in range(h):
        for j in range(n):
            if 0 in arr[i][j]:
                return -1
            if max(arr[i][j]) > res:
                res = max(arr[i][j])
    return res - 1

print(func())