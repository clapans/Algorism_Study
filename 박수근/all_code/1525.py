import sys
from collections import deque

arr = []
for _ in range(3):
    arr.append(list(map(int,sys.stdin.readline().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def find(arr):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == 0:
                return [i,j]

def trans_tuple(arr):
    tmp = []
    for i in range(3):
        tmp.append((arr[i][0],arr[i][1],arr[i][2]))
    return tuple(tmp)

answer = [[1,2,3],[4,5,6],[7,8,0]]
visit = {}
queue = deque([[arr,0]])
while queue:
    tmp_ = queue.popleft()
    arr,cnt = tmp_[0],tmp_[1]
    if arr == answer:
        print(cnt)
        quit(0)
    start = find(arr)
    arr_save = [t[:] for t in arr]
    for t in range(4):
        nx = start[0] + dx[t]
        ny = start[1] + dy[t]
        if 0 <= nx < 3 and 0 <= ny < 3:
            tmp = arr[nx][ny]
            arr[nx][ny] = 0
            arr[start[0]][start[1]] = tmp
            trans = trans_tuple(arr)
            try:
                visit[trans]
            except:
                visit[trans] = 0
                queue.append([arr,cnt+1])
            arr = [t[:] for t in arr_save]
print(-1)