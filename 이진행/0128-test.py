import sys
from pprint import pprint
'''
#가로 세로길이 입력후, 그리드 생성

width, length = map(int, sys.stdin.readline().split())
board = [[0 for _ in range(width)] for _ in range(length)]


#자르는 횟수
num = int(sys.stdin.readline())

#그리드에 1씩 넣어주는 조건
for _ in range(num):
    #0,1 처리
    front, end  = map(int, input().split())
    
    if front == 0:
        for x in range(length-end):
             for y in range(width):
                board[x][y]+=1
    elif front == 1:
        for x in range(length):
            for y in range(width-end):
                board[x][y]+=1
    else:
        pass


    # for x in range(l-r2):
    #     for y in range(r-l1):
    #         board[x][y]=1

#그리드에 채워진 가장 높은 숫자 더하기 ==3 
count = 0
for x in board:
    for y in x:
        if y ==num:
            count+=y/num
 
for i in board:
    for j in i:
        print(j,end=" ")
    print()

print(count)

'''

'''
아이디어 : 자른대로 누적값을 더해서, 최종적으로 가장 많이 누적된 값만 더하기

'''
#가로 세로 입력
width, length = map(int, sys.stdin.readline().split())

#입력받은 값으로 width*length 그리드 생성
board = [[0]*width for _ in range(length)]

#자르는 횟수 입력
num = int(sys.stdin.readline())

#가로, 세로 입력값, 자르는 횟수만큼 반복
for _ in range(num):
    front, end  = map(int, input().split())
    #가로 자르기
    if front == 0:
        #자른 가로의 숫자가 전체 세로길이/2인 경우, 자른 위치부터 전체 세로길이 범위까지 +1
        if end <= length/2:
            for x in range(end, length):
                for y in range(width):
                    board[x][y]+=1
        #자른 가로의 숫자가 세로길이/2보다 큰경우, 처음 위치부터 자른 숫자 범위까지 +1
        else:
            for x in range(end):
                for y in range(width):
                    board[x][y]+=1

    #세로자르기
    elif front == 1:
        #자른 세로의 숫자가 전체 가로의 길이/2인 경우, 자른 세로의 위치부터 전체 가로의 길이 범위까지 +1
        if end <= width/2:
            for x in range(length):
                for y in range(end, width):
                    board[x][y]+=1
        
        #자른 세로의 숫자가 전체 가로의 길이/2보다 큰 경우, 처음 위치부터 자른 숫자 범위까지 +1
        else:
            for x in range(length):
                for y in range(end):
                    board[x][y]+=1
    else:
        pass

#추가한 그리드 중 자른 횟수와 동일한 값만 더한 후, 자른 횟수로 나누어줌
'''
count = 0
for x in board:
    for y in x:
        if y ==num:
            count+=y/num
            '''
count = 0
for x in board:
    for y in x:
        if y ==num:
            count+=y/num

#그리드 깔끔하게 출력    
for i in board:
    for j in i:
        print(j,end=" ")
    print()
print(count)

