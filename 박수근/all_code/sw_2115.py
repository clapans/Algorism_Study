from pprint import pprint

def one_line():
    res = 0
    for i in range(n-1):
        for j in range(i+1,n):
            left = max(dp[i][:i+1])
            right = max(dp[j][i+1:])
            res = max(res,left + right) 
    return res

for case in range(int(input())):
    n,m,c = map(int,input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    ans = [0,0,0]
    for i in range(n):
        res = [0,0]
        dp = [[0]*n for _ in range(n)]
        for j in range(n):
            if arr[i][j] <= c:
                sum_ = arr[i][j]
                tmp = arr[i][j]**2
                cnt = 1
                dp[j][j] = tmp
                while cnt < m:
                    if sum_ + arr[i][j-cnt] <= c:
                        sum_ += arr[i][j-cnt]
                        tmp += arr[i][j-cnt]**2
                        dp[j][j-cnt] = tmp
                        cnt += 1
                    else:
                        break
        #pprint(dp)
        res[0] = max([max(t) for t in dp])
        res[1] = one_line()
        if res[0] > ans[0]:
            ans[1] = ans[0]
            ans[0] = res[0]
        elif res[0] > ans[1]:
            ans[1] = res[0]
        if res[1] > ans[2]:
            ans[2] = res[1]
    print(f'#{case+1} {ans[0]+ans[1]}') 