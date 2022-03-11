def improve_check(arr):
    check_pass = [False] * w
    for i in range(w):
        tmp = 1
        for j in range(1,d):
            if arr[j][i] == arr[j-1][i]:
                tmp += 1
            else:
                tmp = 1
            if tmp >= k:
                check_pass[i] = True
                break
    return check_pass
 
def backtrack(x,cur_atr,cnt):
    global res
    check_pass = improve_check(arr)
    if check_pass == [True] * w:
        res = min(res,cnt)
    else:
        if x < d and cnt < res:
            save = arr[x][:]
            for i in range(2):
                if cur_atr == -1 or i == cur_atr:
                    arr[x][:] = [i] * w
                    backtrack(x+1,i,cnt+1)
                    arr[x][:] = save[:]
            backtrack(x+1,-1,cnt)

for case in range(int(input())):
    d,w,k = map(int,input().split())
    arr = []
    res = int(1e9)
    for _ in range(d):
        arr.append(list(map(int,input().split())))
    backtrack(0,-1,0)
    print(f'#{case+1} {res}')