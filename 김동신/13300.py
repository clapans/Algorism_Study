total_count, k =map(int,input().split())

#성별/학년별로 인원수 체크를 위한 이중리스트 생성
ban=[[0]*6]+[[0]*6]      #[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

#모든 학생들의 정보를 반복하면서 각각에 맞는 곳에 인원 추가
for _ in range(total_count) :
    x,y = map(int,input().split())
    ban[x][y-1] = ban[x][y-1] + 1

#각 인원을 최대 배정 가능 인원으로 나누고 나머지가 남을 경우 몫에 1을 더해줘서 방 하나를 더 추가함.
cnt = 0
for i in ban :
    for j in i :
        if j%k :
            cnt += j//k+1
        else :
            cnt += j//k
print(cnt)
