board = [list(map(int, input().split())) for _ in range(5)] 
call = []
for _ in range(5):
    call += (list(map(int, input(). split())))

real_board = board[::]
V = []
D1 = []
D2 = []



for i in range(5):
    for j in board:
        V.append(j[i])
    real_board.append(V) 
    V = []

for k in range(5):
    D1.append(board[k][k])
    D2.append(board[k][-k-1])
real_board.append(D1)
real_board.append(D2)

cnt = 0
for num in call:
    for l in real_board:
        try:
            l.remove(num)
        except: 
            continue
    cnt += 1
    if real_board.count([]) >= 3:
        print(cnt)
        break



