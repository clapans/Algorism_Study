T = int(input())

def danjo_check(number):
    lst = list(map(int,list(str(number))))

    for i in range(1,len(lst)) :
        if lst[i-1] > lst[i] :
            return -1
    else :
        return 1

for tc in range(T) :
    N = int(input())
    numbers = list(map(int,input().split()))

    danjo = -1
    for i in range(N-1) :
        for j in range(i+1,N) :
            tmp = numbers[i]*numbers[j]
            res = danjo_check(tmp)
            if res == 1 and danjo < tmp :
                danjo = tmp

    print(f"#{tc+1} {danjo}")
