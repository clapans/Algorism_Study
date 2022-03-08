import sys
sys.stdin = open('input.txt')

def check(num):
    a= str(num)
    for k in range(len(a)-1):
        if a[k] > a[k+1]:
            return False
    return True

T = int(input())

for tc in range(1,T+1):
    #입력 숫자
    n = int(input())

    #입력 리스트
    lst1 = list(map(int, input().split()))

    #곱셈 리스트
    lst2=[]
    for a in range(n):
        for j in range(n):
            if a<j:
                if lst1[a]*lst1[j]>10:
                    lst2.append(lst1[a]*lst1[j])

    print(lst1)
    tmp=0
    for a in lst2:
        if check(a):
            tmp = max(tmp,a)



    if tmp==0:
        tmp=-1

    print(f'#{tc} {tmp}')

