from re import A, I
import sys
#빙고문제
# a,b,c,d,e = map(int, sys.stdin.readline().split())
board = {}
check = [[0]*5 for _ in range(5)]
for i in range(5):
    a=list(map(int, sys.stdin.readline().split()))
    for j in range(5):
        board[a[j]]=(i,j)
tick=0
for i in range(5):
    a=list(map(int, sys.stdin.readline().split()))
    for j in range(5):
        tick+=1

        if a[j] in board:
            check[board[]]
    


for i in check:
    for j in i:
        print(j, end=" ")
    print()
