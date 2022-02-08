bingo = [list(map(int,input().split(" "))) for _ in range(5)]
#[[11, 12, 0, 24, 0], [0, 0, 0, 0, 0], [0, 20, 0, 21, 0], [19, 0, 0, 14, 9], [0, 15, 0, 23, 0]]

call_num = []

# 이중리스트x    한번에 받기
for _ in range(5):
    call_num += input().split(" ") 
#[['5', '10', '7', '16', '2'], ['4', '22', '8', '17', '13'], ['3', '18', '1', '6', '25'], ['12', '19', '23', '14', '21'], ['11', '24', '9', '20', '15']]


call_num_list = []
for x in call_num :
    for y in x :
        call_num_list.append(int(y))
#[5, 10, 7, 16, 2, 4, 22, 8, 17, 13, 3, 18, 1, 6, 25, 12, 19, 23, 14, 21, 11, 24, 9, 20, 15]

change_cnt = 0
for i in call_num_list :
    cnt = 0   #빙고 몇개?
    
    #for, range(5) 활용해서 반복문 다시 짜보기
    if bingo[x][y] == i 

    for idx1,j in enumerate(bingo) :
        if i not in j :
            continue
        
        # j = 하나의 가로줄           
        for idx2,k in enumerate(j) :
            if k == i :
                change_cnt += 1
                bingo[idx1][idx2] = 0  #사회자가 말한 숫자를 0으로 바꿔버리기
                break

    if change_cnt >= 12 :
    
    # 가로줄 빙고일 때 찾기 가로줄의 합이 0이면 전부 0이므로 빙고               
        for jool in bingo :
            if not sum(jool) :   #False면 실행
                cnt += 1

    # 세로줄 빙고인 경우 찾기
        for num_y in range(5) :
            tmp = 5
            for num_x in range(5) :       #(x,y)라 할때 y가 고정되고 x를 반복으로 돌림
                if bingo[num_x][num_y] :  #하나라도 0이 아니면 빙고가 될 수 없으므로 바로 break
                    break
                else:                     #0이면 tmp를 차감
                    tmp -= 1
            if not tmp :                  #바뀐 횟수가 5번이면 tmp는 0이되고 빙고라는 뜻
                cnt+=1
                                
        # 대각선인 경우 찾기
        for x in range(5) :
            if bingo[x][x] :    #왼쪽 위에서 오른쪽 아래로 떨어지는 대각선
                break
        else :                  #반복문을 다 돌았으면 전부 0이라는 뜻이기 때문에 cnt 추가
            cnt+=1

        for x in range(5) :
            if bingo[x][4-x] :  #오른쪽 위에서 왼쪽 아래로 떨어지는 대각선
                break
        else :
            cnt+=1  

    if cnt >= 3 :           # 3빙고!
        print(change_cnt)   # 바뀐 횟수 = 사회자가 숫자 몇개 부름?
        break