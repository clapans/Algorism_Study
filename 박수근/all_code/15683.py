import sys

n,m = map(int,sys.stdin.readline().split())
arr = []
camera = {
    1 : [0],
    2 : [0,2],
    3 : [0,3],
    4 : [0,2,3],
    5 : [0,1,2,3]
}

dir = {
    0 : [0,1],
    1 : [-1,0],
    2 : [0,-1],
    3 : [1,0]
}

for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

cameraList = []

for i in range(n):
    for j in range(m):
        if 1 <= arr[i][j] <= 5:
            cameraList.append([i,j,arr[i][j]])

res = n*m

def watchCase(v):
    global res
    global arr
    if v == len(cameraList):
        res = min(res,cntWatch())
    else:
        arr_save = copyArr(arr)
        x,y,num = cameraList[v]
        cam = camera[num]
        for i in range(4):
            if i == 1 and num == 5:
                break
            if i == 2 and num == 2:
                break
            for j in cam:
                watch(x,y,dir[j])
            watchCase(v+1)
            arr = copyArr(arr_save)
            cam = rotate(cam)

def watch(x,y,dir):
    x += dir[0]
    y += dir[1]
    while 0 <= x < n and 0 <= y < m and arr[x][y] != 6: 
        if arr[x][y] == 0:
            arr[x][y] = "#"
        x += dir[0]
        y += dir[1]

def rotate(cam):
    for i in range(len(cam)):
        cam[i] = (cam[i]+1) % 4
    return cam

def copyArr(arr):
    newArr = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            newArr[i][j] = arr[i][j]
    return newArr

def cntWatch():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1
    return cnt

watchCase(0)
print(res)