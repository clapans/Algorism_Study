import sys
sys.stdin = open('input.txt')

N = int(input())

board = list(map(int, input().split()))
ord_num = int(input())
ord_board = list(input().split())

for i in range(ord_num):
    if ord_board[i] == 'I':
        board.insert(board[i+1], board[i+3]*board[i+2])
    elif ord_board[i] == 'D':
        del board[ord_board[i+1]:ord_board[i+2]+1]
    elif ord_board[i] == 'A':

    else:
        continue



print(*board)
print(*ord_board)