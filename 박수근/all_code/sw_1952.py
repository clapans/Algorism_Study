def one_month(x):
    return min(date[x] * price[0], price[1])

for case in range(int(input())):
    price = list(map(int,input().split()))
    date = list(map(int,input().split()))
    dp = [0] * 12
    dp[0] = one_month(0)
    dp[1] = dp[0] + one_month(1)
    dp[2] = min(price[2],dp[1] + one_month(2))
    for i in range(3,12):
        dp[i] = min(dp[i-3] + price[2],dp[i-1] + one_month(i))
        if i == 11:
            dp[i] = min([price[3],dp[i],dp[i-2] + price[2]])
    print(f'#{case+1} {dp[-1]}')