# 😇SWEA4615 재미있는 오셀로

## 👺필요한 개념

- 좌표순회, 뒤집어주는것 구현, while문 활용, 델타탐색

## 👺풀이과정

- 처음에 고정되어있는 백돌,흑돌 설정

- 델타 탐색으로 조건을 구분

  

- 한 후, 뒤집어주는 배열을 따로 저장한다음 while문이 끝날때 뒤집어주는걸 실행한다.

- 마지막에 백돌,흑돌 검색

## 👺코드

```python
num = int(sys.stdin.readline())

for tc in range(1,num+1):

    N, M = map(int, input().split())
    #빈 배열 바둑판 생성
    board = [[0]*N for _ in range(N)]
    # 8가지 방향을 탐색 상,하,좌,우,우좌,우상,좌하,좌상
    delta = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, -1), (-1, 1)]
    n = N//2
    #초기값 설정
    #2 = 백돌 , 1 = 흑돌
    board[n-1][n-1]=2
    board[n-1][n]=1
    board[n][n-1]=1
    board[n][n]=2
    
    for _ in range(M):
        x,y,z = map(int, input().split())
        y,x = y-1,x-1
        board[x][y] =z
        
        # 뒤집을 좌표 리스트
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
                #공백확인시 멈춤
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
        
     
	#백돌,흑돌 탐색
    W, B = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                W+=1
            elif board[i][j] ==2:
                B+=1
    
    print(f'#{tc} {W} {B}')

```

