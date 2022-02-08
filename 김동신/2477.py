count = int(input())
farm = [list(map(int,input().split(" "))) for _ in range(6)]

loc = [] #[50, 160, 30, 60, 20, 100]
loc_y = []
loc_x = []

#남 or 북이면 y로 동or서면 x로 추가
for x in farm :
    loc.append(x[1])
    if x[0] == 3 or x[0] == 4 :
        loc_y.append(x[1])
    else :
        loc_x.append(x[1])

# 전체 사각형
big_square = max(loc_y) * max(loc_x)

# 가로 세로 각 최댓값의 위치
base_y = loc.index(max(loc_y))
base_x = loc.index(max(loc_x))

#가장 큰 값을 기준으로 인접한 두개의 차이 구하기
small_y = abs(loc[base_y-1] - loc[0 if base_y == 5 else base_y+1])
small_x = abs(loc[base_x-1] - loc[0 if base_x == 5 else base_x+1])

result = (big_square - (small_y*small_x)) * count
print(result)
print(loc)