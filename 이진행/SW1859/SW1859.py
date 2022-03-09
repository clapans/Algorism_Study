import sys
sys.stdin = open('input.txt')

num = int(input())

for tc in range(1,num+1):
    N = int(input())
    board = list(map(int, input().split()))
    _max = board[-1]
    cnt=0
    for i in range(N-2,-1,-1):
        if _max < board[i]:
            _max = board[i]
        else:
            cnt+= _max - board[i]

    print(f'#{tc} {cnt}')