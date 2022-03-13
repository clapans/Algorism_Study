def processing_a(arr,loc,W) :
    arr[loc] = [0]*W
    return arr

def processing_b(arr,loc,W):
    arr[loc] = [1]*W
    return arr


def check_pass(arr,W,D,K) :
    global res
    check = []
    check_point =[]
    point = 0
    for j in range(W):
        cnt=1
        tmp = 0
        for i in range(1,D):
            if arr[i-1][j] == arr[i][j] :
                cnt+=1
                if tmp < cnt :
                    tmp = cnt
                    point = i
            else :
                cnt=1
        check.append(tmp)
        check_point.append(point)
    if min(check) >= K :
        return res
    else :
        loc = check_point[check.index(min(check))]
        res += 1
        new_arr = processing_a(arr,loc,W)
        return check_pass(new_arr,W,D,K)




arr = [list(map(int,input().split())) for _ in range(6)]
res=0
ans = check_pass(arr,8,6,3)
print(ans)