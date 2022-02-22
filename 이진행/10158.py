

# row, col 인덱스로 탐색할 수 있게 방향 설정 (달팽이 방향이니까 우->하->좌->상)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


w,h = map(int,input().split())
x, y = (map(int, input().split()))
T = int(input())
# snail = [[0]*N for _ in range(L)]
# # 초기 위치 & 회전방향 설정
# r, c = 0, 0
# dist = 0  # 0:우, 1:하, 2:좌, 3:상



xt = x+T
yt = y+T
print(xt%2*w, yt%2*h)