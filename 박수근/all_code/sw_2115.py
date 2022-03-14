def cal_square(bit,arr):
    tmp = 0
    sum_ = 0
    for t in range(m):
        if bit[t] == '1':
            sum_ += arr[t]
            tmp += arr[t] ** 2
    if sum_ <= c:
        return tmp
    return 0
    
def one_line(t,bit,i):
    global res
    if t == n-1:
        if bit.count('1') <= m:
            res = max(res,cal_square(bit,arr[i][:]))
    else:
        one_line(t+1,bit,i)
        bit[t] = '1'
        one_line(t+1,bit,i)
        
for case in range(int(input())):
    n,m,c = map(int,input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    ans = [0,0]
    for i in range(n):
        res = 0
        one_line(0,[0]*n,i)
        if res > ans[0]:
            ans[1] = ans[0]
            ans[0] = res
        elif res > ans[1]:
            ans[1] = res

    print(f'#{case+1} {ans[0]+ans[1]}') 