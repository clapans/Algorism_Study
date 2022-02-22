import sys
sys.stdin = open('input.txt')
N,K = map(int, sys.stdin.readline().split())

board = [[0]*2 for _ in range(1,7)]

for _ in range(N):
    S, Y = map(int, sys.stdin.readline().split())
    board[Y-1][S-1] +=1

print(board)