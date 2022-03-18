oper_dict = {0 : '+', 1 : '-', 2 : '*', 3 : '/'}

def cal(a,b,operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:
        return int(a/b)

def dfs(x,use):
    if dp[x][use]:
        return dp[x][use]
    min_tmp,max_tmp = int(1e9),-int(1e9)
    for t in range(4):
        tmp = str(use)
        while len(tmp) < 4:
            tmp = "0" + tmp
        if int(tmp[t]) + 1 <= operator[t]:
            use += 10**(3-t)
            operand = dfs(x-1,use)
            min_tmp = min(min_tmp,cal(operand[0],nums[x],oper_dict[t]))
            max_tmp = max(max_tmp,cal(operand[1],nums[x],oper_dict[t]))
            use -= 10**(3-t)
    dp[x][use] = (min_tmp,max_tmp)
    return dp[x][use]

for case in range(int(input())):
    n = int(input())
    operator = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    if sum(operator) in operator:
        print(f'#{case+1} {0}')
        continue
    elif 10 in operator:
        oper_a = oper_dict[operator.index(10)]
        oper_b = oper_dict[operator.index(1)]
        min_res,max_res = int(1e9), -int(1e9)
        for i in range(1,n):
            tmp = nums[0]
            for j in range(1,n):
                if j == i:
                    tmp = cal(tmp,nums[j],oper_b)
                else:
                    tmp = cal(tmp,nums[j],oper_a)
            min_res = min(min_res,tmp)
            max_res = max(max_res,tmp)
        print(f'#{case+1} {max_res - min_res}')
        continue
    dp = [[0]*9999 for _ in range(n)]
    trans_oper = list(map(str,operator))
    dp[0][int(''.join(trans_oper))] = (nums[0], nums[0])
    min_res,max_res = dfs(n-1,0)
    print(f'#{case+1} {max_res - min_res}')
