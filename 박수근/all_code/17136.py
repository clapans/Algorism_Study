import sys

def is_check(x,y,n,arr):
    if x+n > 10 or y+n > 10:
        return False
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j] == 0:
                return False
    return True

def fill_arr(x,y,n,value):
    for i in range(x,x+n):
        for j in range(y,y+n):
            arr[i][j] = value
        
def dfs(x,y,use,cnt):
    global res
    while (x < 10 and arr[x][y] == 0):
        if y == 9:
            x += 1
            y = 0
        else:
            y += 1
    if x == 10:
        res = min(res,cnt)
    else:
        for t in range(1,6):
            if use[t-1] > 0 and is_check(x,y,t,arr):
                fill_arr(x,y,t,0)
                use[t-1] -= 1
                if y == 9:
                    dfs(x+1,0,use,cnt+1)
                else:
                    dfs(x,y+1,use,cnt+1)
                use[t-1] += 1
                fill_arr(x,y,t,1)

arr = []

for _ in range(10):
    arr.append(list(map(int,sys.stdin.readline().split())))    

res = int(1e9)
dfs(0,0,[5,5,5,5,5],0)
if res == int(1e9):
    print(-1)
else:
    print(res)