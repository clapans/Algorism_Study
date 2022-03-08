import sys
sys.stdin = open('input.txt')



T = int(input())

for tc in range(1):
    #입력 숫자
    n = int(input())

    #입력 리스트
    lst=[]
    for _ in range(n):
        lst.append(list(map(int, input().split())))

    for a in lst:
        for b in a:
            print(b,end=" ")
        print()
    #print(f'#{tc} {tmp}')

