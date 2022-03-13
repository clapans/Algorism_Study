from pprint import pprint
import sys
sys.stdin = open("input.txt")


# def k_range(arr,x,y,k,N):
#     dx=[0,0,-1,1]
#     dy=[1,-1,0,0]
#     if k == 1 :
#         if arr[x][y] == 1 :
#             arr[x][y] = 5
#
#     else :
#         if arr[x][y]==1 :
#             arr[x][y] = 5
#         for i in range(4) :
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<N and 0<=ny<N :
#                 if arr[nx][ny] == 1 :
#                     arr[nx][ny] = 5
#
#                 k_range(arr,nx,ny,k-1,N)

# 새로운 마름모 범위 구하는 공식
# 기준점 위아래로 한칸씩 이동할 때마다 좌우 하나씩 줄어든다
def k_range2_down(arr,x,y,k,N):
    cnt_down = 0
    while k>0:
        for K in range(k) :
            ny_1 = y+K
            if 0<=x<N and 0<=ny_1<N and arr[x][ny_1] == 1 :
                arr[x][ny_1] = 5
                cnt_down += 1
            ny_2 = y-K
            if 0<=x<N and 0<=ny_2<N and arr[x][ny_2] == 1 :
                arr[x][ny_2] = 5
                cnt_down += 1
        x += 1
        k -= 1
    return cnt_down

def k_range2_up(arr,x,y,k,N):
    cnt_up = 0
    while k>0:
        for K in range(k) :
            ny_1 = y+K
            if 0<=x<N and 0<=ny_1<N and arr[x][ny_1] == 1 :
                arr[x][ny_1] = 5
                cnt_up += 1
            ny_2 = y-K
            if 0<=x<N and 0<=ny_2<N and arr[x][ny_2] == 1 :
                arr[x][ny_2] = 5
                cnt_up += 1
        x -= 1
        k -= 1
    return cnt_up


T = int(input())
for tc in range(T) :
    N,M = map(int,input().split())
    arr_origin = [list(map(int,input().split())) for _ in range(N)]

    home = 0
    for home_i in range(N):
        for home_j in range(N):
            if arr_origin[home_i][home_j] == 1 :
                home += 1

    maximum = home*M
    cost_max=0
    k_max=0
    while cost_max < maximum :
        k_max += 1
        cost_max = k_max*k_max+(k_max-1)*(k_max-1)



    res=0
    for k in range(1,k_max) :
        for i in range(N):
            for j in range(N) :
                arr = [item[:] for item in arr_origin]
                ans1 = k_range2_up(arr,i,j,k,N)
                ans2 = k_range2_down(arr,i,j,k,N)
                # for i2 in range(N):
                #     for j2 in range(N):
                #         if arr[i2][j2] == 5 :
                #             cnt += 1
                cost =  k*k+(k-1) * (k-1)
                revenue = M*(ans1+ans2) - cost
                if revenue>=0 and ans1+ans2 > res :
                    res = ans1+ans2

    print(f'#{tc+1} {res}')