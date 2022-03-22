def food(x,v,cnt):
    global res
    if cnt == n//2:
        lst1 = [ix for ix,val in enumerate(v) if val == 1]
        lst2 = [ix for ix,val in enumerate(v) if val == 0]
        res = min(res,abs(cal(lst1)-cal(lst2)))
    elif x < n:
        v[x] = 1
        food(x+1,v,cnt+1)
        v[x] = 0
        food(x+1,v,cnt)

def cal(v):
    tmp = 0
    for i in range(len(v)-1):
        for j in range(i+1,len(v)):
            tmp += synergy[v[j]][v[i]]
            tmp += synergy[v[i]][v[j]]
    return tmp

for case in range(int(input())):
    n = int(input())
    synergy = []
    for _ in range(n):
        synergy.append(list(map(int,input().split())))
    res = int(1e9)
    food(0,[0]*n,0)
    print(f'#{case+1} {res}')

'''
def food(x,v,cnt):
    if cnt == n//2:
        res.append(v)
    elif x < n and cnt < n//2:
        tmp = 0
        for i in range(x):
            if 2**i & v:
                tmp += synergy[x][i]
                tmp += synergy[i][x]

        dp[2**x | v] = dp[v] + tmp
        food(x+1,2**x | v,cnt+1)
        food(x+1,v,cnt)

for case in range(int(input())):
    n = int(input())
    synergy = []
    for _ in range(n):
        synergy.append(list(map(int,input().split())))
    dp = [0] * (1 << n)
    res = []
    food(0,0,0)
    result = int(1e9)
    for i in range(len(res)):
        result = min(result,abs(dp[res[i]] - dp[2**n-res[i]-1]))
    
    print(f'#{case+1} {result}')
'''