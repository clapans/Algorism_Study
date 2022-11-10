n = input()

dp = [[0]*2 for _ in range(len(n))]

if n[0] == '0':
    print(0)
    quit()

if len(n) == 1:
    print(1)
    quit()
    
dp[0][0] = 1
dp[0][1] = 0

if n[1] != '0':
    dp[1][0] = 1
else:
    dp[1][0] = 0

if 10 <= int(n[0:2]) <= 26:
    dp[1][1] = 1
else:
    dp[1][1] = 0

for t in range(2,len(n)):
    if n[t] != '0':
        dp[t][0] = sum(dp[t-1]) % 1000000
    else:
        dp[t][0] = 0
    if 10 <= int(n[t-1:t+1]) <= 26:
        dp[t][1] = sum(dp[t-2]) % 1000000
    else:
        dp[t][1] = 0

print(sum(dp[-1]) % 1000000)