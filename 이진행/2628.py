import sys
"""
width, length = map(int, sys.stdin.readline().split())
board = [[0]*width for _ in range(length)]
num = int(sys.stdin.readline())
for _ in range(num):
    front, end  = map(int, input().split())
    if front == 0:
        if end <= length/2:
            for x in range(end, length):
                for y in range(width):
                    board[x][y]+=1
        else:
            for x in range(end):
                for y in range(width):
                    board[x][y]+=1
    elif front == 1:
        if end <= width/2:
            for x in range(length):
                for y in range(end, width):
                    board[x][y]+=1
        else:
            for x in range(length):
                for y in range(end):
                    board[x][y]+=1
    else:
        pass
count = 0
for x in board:
    for y in x:
        if y ==num:
            count+=y/num
print(int(count))
"""
x, y = map(int, input().split())
x_list = [0, x] #가로 각각 길이
y_list = [0, y] #세로 각각 길이
for _ in range(int(input())):
    xy, length = map(int, input().split())
    if xy == 0:
        y_list.append(length)
    else:
        x_list.append(length)
        
x_list.sort() #좌, 위쪽부터 꺼내서 대조 하기 위함
y_list.sort()

max_square = 0
for i in range(1, len(x_list)):
    for j in range(1, len(y_list)):
        width = x_list[i] - x_list[i-1]
        height = y_list[j] - y_list[j-1]
        max_square = max(max_square, width * height) #가장 큰 범위

print(max_square)