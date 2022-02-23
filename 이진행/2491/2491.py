import sys
sys.stdin = open('input.txt')


for ca in range(1,4):
    N = int(input())
    K = list(map(int, input().split()))


    #비교할 값
    cnt = 1
    max_1 = 1

    #탐색, 수열 커지는 방향
    for a in range(1,N):
        if K[a]>=K[a-1]:
            cnt+=1
        else:
            cnt=1

        #가장 큰 값 도출
        if max_1 < cnt:
            max_1 = cnt


    #탐색, 수열 작아지는 방향
    for a in range(1,N):
        if K[a] <=K[a-1]:
            cnt+=1
        else:
            cnt=1

        #가장 큰 값 도출
        if max_1 < cnt:
            max_1 = cnt


    print(max_1)

    #print(*arr2)
    # print(f'{ca} {K}')

