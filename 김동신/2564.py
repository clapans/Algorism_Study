x,y = map(int,input().split())
N=int(input())

# 점의 개수를 기준으로 빈 리스트 생성
x1,x2,y1,y2 = [0]*(x+1),[0]*(x+1),[0]*(y+1),[0]*(y+1)

#위치를 받아서 리스트에 추가 (처음 들어오는 상점은 1번, 다음은 2번, 맨 마지막은 경찰)
for n in range(1,N+2) :
    tmp = list(map(int,input().split()))
    if tmp[0] == 1 :
        x1[tmp[1]] = n
    elif tmp[0] == 2 :
        x2[tmp[1]] = n
    elif tmp[0] == 3 :
        y1[tmp[1]] = n
    elif tmp[0] == 4 :
        y2[tmp[1]] = n

#서쪽과 남쪽 줄은 역순으로 진행 그리고 양 옆줄은 양쪽 끝을 제외한 값들만 추가
#경비원과의 최단거리를 구하기 위해 3개 곱해줌
loc = (x1+y2[1:-1]+x2[::-1]+y1[-2:0:-1])*3

#블록의 총 둘레
length = (x+1+y-2)*2

#중간 경찰의 위치 파악
police = loc.index(N+1,length)
res = []

#상점별로 거리를 측정(3개) 그 중 가장 짧은 거리를 결과값에 추가
for store in range(1,N+1) :
    distance = []
    for i in range(3) :
        store_loc = loc.index(store,(length)*i)
        distance.append(abs(police-store_loc))
    res.append(min(distance))

#이후 덧셈
print(sum(res))

