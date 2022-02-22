import sys

board = [[0 for _ in range(1001)] for _ in range(1001)]
num = int(sys.stdin.readline())

#숫자 넣어주기
for i in range(1,num+1):
    x, y, w, h = map(int, input().split())
    for y in range(y,y+h):
        board[y][x:x+w] = [i] * w

#넣은 숫자 카운트하고 더하기
for p in range(1, num+1):
    res = 0
    for ct in range(1001):
        res+=board[ct].count(p)
    print(res)
