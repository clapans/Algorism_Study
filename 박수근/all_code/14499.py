n,m,x,y,k = map(int,input().split())
arr = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for _ in range(n):
    arr.append(list(map(int,input().split())))

command = list(map(int,input().split()))

dice = [0]*6

def diceMove(x):
    if x == 1:
        tmp = dice[4]
        dice[4] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[0]
        dice[0] = tmp
    elif x == 2:
        tmp = dice[5]
        dice[5] = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[0]
        dice[0] = tmp
    elif x == 3:
        tmp = dice[3]
        dice[3] = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[0]
        dice[0] = tmp
    else:
        tmp = dice[2]
        dice[2] = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[0]
        dice[0] = tmp

for c in command:
    if 0 > x + dx[c-1] or x + dx[c-1] >= n or 0 > y + dy[c-1] or y + dy[c-1] >= m:
        continue 
    diceMove(c)
    x += dx[c-1]
    y += dy[c-1]
    if arr[x][y] == 0:
        arr[x][y] = dice[1]
    else:
        dice[1] = arr[x][y]
        arr[x][y] = 0
    print(dice[0])      