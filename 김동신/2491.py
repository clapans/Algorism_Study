def Increasing(arr,N) :
    result = 0
    i=0
    tmp=1
    while i < N-1 :
        if arr[i] <= arr[i+1] :
            tmp+=1
            i+=1
        else :
            i=i+1
            if result < tmp :
                result = tmp
            tmp = 1
    if result < tmp:
        result = tmp

    return result

def Decreasing(arr,N) :
    result = 0
    i=0
    tmp=1
    while i < N-1 :
        if arr[i] >= arr[i+1] :
            tmp+=1
            i+=1
        else :
            i=i+1
            if result < tmp :
                result = tmp
            tmp = 1
    if result < tmp:
        result = tmp

    return result


N = int(input())
lst = list(map(int,input().split()))
# 증가하는 수들의 가장 큰 길이
cnt_up = Increasing(lst,N)

# 감소하는 수들의 가장 큰 길이
cnt_down = Decreasing(lst,N)

# 둘 중 큰거를 출력
answer = cnt_up if cnt_up > cnt_down else cnt_down
print(answer)

