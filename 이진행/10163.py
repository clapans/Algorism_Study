import sys
from pprint import pprint

num = int(input())

if num == 2:
    count1 = 0
    count2 = 0
    board=[[0]*101 for _ in range(102)]
    for a in range(num):
        x, y, w, h = map(int, input().split())
        for i in range(x,x+w):
            for j in range(y,y+h):
                board[i][j]=a+1
        # for x in board:
        #     for y in x:
        #         if y == 1:
        #             count1 += y
        #         elif y == 2:
        #             count2 += y / y

        for x in board:
            if y == 1:
                count1 += y
            elif y == 2:
                count2 += y / y



    print(count1)
    print(int(count2))

    # for x in board:
    #     for y in x:
    #         print(y, end="")
    #     print()

    # for x in board:
    #     for y in x:
    #         if y==1:
    #             count1+=y
    #         elif y==2:
    #             count2+=y/y
    #         # elif: y==3:
    #         #     count3+=y/y

elif num == 3:
    count1 = 0
    count2 = 0
    count3 = 0
    board = [[0] * 101 for _ in range(102)]
    for a in range(num):
        x, y, w, h = map(int, input().split())
        for i in range(x, x + w):
            for j in range(y, y + h):
                board[i][j] = a + 1

    for x in board:
        for y in x:
            if y == 1:
                count1 += y
            elif y == 2:
                count2 += y / y
                int(count2)
            # elif: y==3:
            #     count3+=y/y
            elif y > 2:
                count3 += y / y

    print(count1)
    print(count2)
    print(count3)


elif num == 1:
    count1 = 0
    board = [[0] * 101 for _ in range(102)]
    x, y, w, h = map(int, input().split())
    for i in range(x, x + w):
        for j in range(y, y + h):
            board[i][j] = 1
    count1 = 0
    for x in board:
        for y in x:
            count1 += y
    print(count1)
else:
    list1=[]
    count2=0
    count3=0
    count4=0


    board = [[0]*1001 for _ in range(1002)]
    for a in range(num):
        x, y, w, h = map(int, input().split())
        for i in range(x, x + w):
            for j in range(y, y + h):
                board[i][j] =a+1

        for x in board:
            for y in x:
                if y==a+1:
                    count2+=int(y/y)
                    list1.append(count2)


        print(list1)

#
# # for i in board:
# #     for j in i:
# #         print(j,end=" ")
# #     print()