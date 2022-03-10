def improve_check(arr):
    for i in range(w):
        tmp = 1
        check_pass[i] = False
        for j in range(1,d):
            if arr[j][i] == arr[j-1][i]:
                tmp += 1
            else:
                tmp = 1
            if tmp >= k:
                check_pass[i] = True
                break

def change_check(pre_arr,arr):
    for i in range(w):
        if pre_arr[i] == False and arr[i] == True:
            return True
    return False

def backtrack(x,cur_arr,cnt):
    global res
    if x == d:
        improve_check(cur_arr)
        if check_pass == [True] * w:
            res = min(res,cnt)
    else:
        arr_save = [t[:] for t in cur_arr]
        for i in range(2):
            cur_arr[x][:] = [i] * w
            pre_check_pass = check_pass[:]
            improve_check(cur_arr)
            if change_check(pre_check_pass,check_pass):
                backtrack(x+1,cur_arr,cnt+1)
            cur_arr = [t[:] for t in arr_save]
        backtrack(x+1,cur_arr,cnt)

for case in range(int(input())):
    d,w,k = map(int,input().split())
    arr = []
    res = int(1e9)
    for _ in range(d):
        arr.append(list(map(int,input().split())))
    check_pass = [False] * w
    backtrack(0,arr,0)
    print(f'#{case+1} {res}')