import sys
sys.stdin = open("input.txt")

"""def toojaga_answer(price):
    if len(price) <= 1 :
        return 0
    else:
        global income
        gojum = max(price)
        buy_loc = 0
        sell_loc = price.index(gojum)
        basket = price[buy_loc:sell_loc]
        income += gojum * len(basket) - sum(basket)
        return toojaga_answer(price[sell_loc + 1:])"""



TC = int(input())

for tc in range(TC) :
    N = int(input())
    price = list(map(int,input().split()))
    income = 0
    #toojaga_answer(price)
    while len(price) > 1:
        gojum = max(price)
        buy_loc = 0
        sell_loc = price.index(gojum)
        basket = price[buy_loc:sell_loc]
        income += gojum * len(basket) - sum(basket)
        price = price[sell_loc + 1:]
    print(f'#{tc+1} {income}')




