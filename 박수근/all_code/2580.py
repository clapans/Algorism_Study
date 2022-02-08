import sys

sdoku = []
left = []

for i in range(9):
    sdoku.append(list(map(int,sys.stdin.readline().split())))

def garo(x,i):
    for t in range(9):
        if i == sdoku[x][t]:
            return False
    return True

def sero(y,i):
    for t in range(9):
        if i == sdoku[t][y]:
            return False
    return True

def daegak(x,y,i):
    trans_dict = {0 : [0,1,2], 1 : [3,4,5], 2 : [6,7,8]}
    for t in trans_dict[x//3]:
        for v in trans_dict[y//3]:
            if i == sdoku[t][v]:
                return False
    return True

def func(v):
    if v == len(left):
        for i in range(9):
            print(*sdoku[i])
        exit(0)
    for i in range(1,10):
        x = left[v][0]
        y = left[v][1]
        if garo(x,i) and sero(y,i) and daegak(x,y,i):
            sdoku[x][y] = i
            func(v+1)
            sdoku[x][y] = 0        

for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            left.append([i,j])

func(0)

