import sys
sys.stdin = open('input.txt')



T = int(input())

for tc in range(1,T+1):
    #입력 리스트
    lst1 = []
    for i in range(5):
        lst1.append(input())

    print(lst1)

    #가로로 가장 긴값 찾기
    max_len = 0
    for r in lst1:
        if len(r)>max_len:
            max_len = len(r)

    #가장 긴값 보다 해당 입력 길이가 작으면 추가X
    stp = ''
    for i in range(max_len):
        for j in range(5):
            if i < len(lst1[j]):
                stp+=lst1[j][i]
    print(f'#{tc} {stp}')

