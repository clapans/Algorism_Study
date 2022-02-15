N = int(input())

for _ in range(N) :
    # 맨 앞은 개수이기 때문에 제외
    a_card = list(map(int,input().split()))[1:]
    b_card = list(map(int,input().split()))[1:]

    a_count = [0]*4
    b_count = [0]*4

    for a in a_card :
        a_count[a-1] += 1
    for b in b_card :
        b_count[b-1] += 1

    for i in range(3,-1,-1) :
        if a_count[i] > b_count[i] :
            print("A")
            break
        elif a_count[i] < b_count[i] :
            print("B")
            break
    else :
        print("D")


"""    # 가장 큰 수가 다를 경우 큰 수가 있는 쪽의 승리
    if max(a_card) > max(b_card):
        print("A")
    elif max(a_card) < max(b_card):
        print("B")

    # 가장 큰 수가 같을 경우
    else :
        base = max(a_card)

        while base>0:
            # 가장 큰 수의 개수로 승자 판단
            if a_card.count(base) > b_card.count(base) :
                print("A")
                break
            elif a_card.count(base) < b_card.count(base) :
                print("B")
                break

            # 없으면 가장 큰 수에서 1을 빼줘서 다음 큰 수로 판단
            else :
                base-=1

                # 기준점이 0이 되면 무승부
                if base==0 :
                    print("D")"""