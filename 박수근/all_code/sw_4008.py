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
    if dp[use[0]][use[1]][use[2]][use[3]]:
        return dp[use[0]][use[1]][use[2]][use[3]]
    min_tmp,max_tmp = int(1e9),-int(1e9)
    use_save = use[:]
    for t in range(4):
        if use[t] + 1 <= operator[t]:
            use[t] += 1
            operand = dfs(x-1,use)
            min_tmp = min(min_tmp,cal(operand[0],nums[x],oper_dict[t]))
            max_tmp = max(max_tmp,cal(operand[1],nums[x],oper_dict[t]))
            use = use_save[:]
    dp[use[0]][use[1]][use[2]][use[3]] = (min_tmp,max_tmp)
    return dp[use[0]][use[1]][use[2]][use[3]]

for case in range(int(input())):
    n = int(input())
    operator = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    dp = [[[[0 for i in range(12)] for j in range(12)] for k in range(12)] for l in range(12)]
    dp[operator[0]][operator[1]][operator[2]][operator[3]] = (nums[0],nums[0])
    min_res,max_res = dfs(n-1,[0,0,0,0])
    print(f'#{case+1} {max_res - min_res}')