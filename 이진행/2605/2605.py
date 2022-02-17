import sys
sys.stdin = open('input.txt')

num = int(input())
w = list(map(int, input().split(" ")))
board=[]

for i in range(num):
    board.insert(i-w[i],i+1)

print(*board)











