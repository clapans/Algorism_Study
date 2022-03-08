import sys
sys.stdin = open('input.txt')

#케이스입력
num = int(input())

for tc in range(1,num+1):
    # N = len(Aj) M = len(Bj)
    N,M = map(int,input().split())

    #숫자리스트
    Aj = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    #Aj가 항상 길이가 작은값으로 만들어주기
    if len(Aj) > len(Bj):
        Bj, Aj = Aj, Bj
        N, M = M, N

    #초기값
    cnt=0
    _max=0

    #덧셉작업
    for i in range(M-N+1):
        tmp = 0

        for j in range(N):
            tmp+=Aj[j]*Bj[j+i]

        #최대값 찾기
        if tmp>_max:
            _max=tmp
    #출력
    print(f'#{tc} {_max}')

