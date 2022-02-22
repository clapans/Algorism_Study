


# w, l = map(int, input().split())
# number = int(input())
#
# count =0
# greed = [-1,0,0,0]
# a=-1
# b=0
# c=0
# d=0
#
#
# for x in range(1, w*l+1):
#     count+=1
#     if count%4==1:
#         a+=x
#     elif count%4==2:
#         b+=x
#     elif count%4==3:
#         c+=x
#     else:
#         d+=x
#
#
# print(greed.extends([1,1,1,1]))
#
# w, l = map(int,input().split())
# k = int(input())
# greed = [[0]*w for _ in range(l)]
#
#
# if w * l < k:
#     print(0)
#
# dx , dy =  [-1,0,1,0], [0,1,0,-1]
#
# x,y, dir = l-1,0,0
# cnt = 1
#
# while cnt != k:
#     greed[x][y] = cnt
import sys


T = int(input())

# row, col 인덱스로 탐색할 수 있게 방향 설정 (달팽이 방향이니까 우->하->좌->상)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


N,L = int(input().split())
snail = [[0]*N for _ in range(L)]
# 초기 위치 & 회전방향 설정
r, c = 0, 0
dist = 0  # 0:우, 1:하, 2:좌, 3:상

for n in range(1, N*L + 1):
    snail[r][c] = n
    r += dr[dist]
    c += dc[dist]

    # 범위를 벗어나거나 0이 아닌 다른 값이 이미 있다면, dist 방향 체인지
    # 근데 이런 경우라면 요소 인덱스를 다시 원위치시켜줘야하므로 빼줘야함
    # 그런다음 dist의 방향을 바꾸고, 방향 바꿨으면 다시 움직일 수 있도록 행렬 인덱스 업데이트
    if r < 0 or c < 0 or r >= N or c >= N or snail[r][c] != 0:
        # 실행취소
        r -= dr[dist]
        c -= dc[dist]
        # dist는 % 4 안해주면 0123, 4567, ... 이런식으로 숫자 커지므로 나머지로 접근
        dist = (dist + 1) % 4
        #  다시 gogo
        r += dr[dist]
        c += dc[dist]


for row in snail:
    print(*row)
print()