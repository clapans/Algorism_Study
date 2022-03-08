import sys
sys.stdin = open('input.txt')

num = int(sys.stdin.readline())

for tc in range(1,num+1):

    N, M = map(int, input().split())
    #빈 배열 바둑판 생성
    board = [[0]*N for _ in range(N)]
    # 8가지 방향을 담음
    delta = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, -1), (-1, 1)]
    n = N//2
    #2 = 백돌 , 1 = 흑돌
    board[n-1][n-1]=2
    board[n-1][n]=1
    board[n][n-1]=1
    board[n][n]=2


    for _ in range(M):
        x,y,z = map(int, input().split())
        y,x = y-1,x-1
        board[x][y] = z
        # 뒤집을 좌표
        res = []
        for i in range(8):
            #[(1, 0), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, -1), (-1, 1)]
            dx,dy = delta[i]
            nx, ny = x+dx, y+dy

            while True:
                #범위 벗어나면 멈춤
                if nx<0 or N-1<nx or ny<0 or N-1<ny:
                    res=[]
                    break
                #공백확인시 멈충
                if board[nx][ny] == 0:
                    res = []
                    break
                #같은 색깔 멈춤
                if board[nx][ny] == z:
                    break
                else:
                    res.append((nx,ny))
                nx, ny = nx+dx, ny+dy


            for rx,ry in res:
                if z==1:
                    board[rx][ry]=1
                else:
                    board[rx][ry]=2

        for a in board:
            for b in a:
                print(b, end= " ")
            print()
        print()


    W, B = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                W+=1
            elif board[i][j] ==2:
                B+=1
    print(f'#{tc} {W} {B}')



