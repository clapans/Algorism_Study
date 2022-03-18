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
    if x == 0:
        return (nums[0],nums[0])
    min_tmp,max_tmp = int(1e9),-int(1e9)
    use_save = use[:]
    for t in range(4):
        if use[t] + 1 <= operator[t]:
            use[t] += 1
            operand = dfs(x-1,use)
            min_tmp = min(min_tmp,cal(operand[0],nums[x],oper_dict[t]))
            max_tmp = max(max_tmp,cal(operand[1],nums[x],oper_dict[t]))
            use = use_save[:]
    return (min_tmp,max_tmp)
 
for case in range(int(input())):
    n = int(input())
    operator = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    min_res,max_res = dfs(n-1,[0,0,0,0])
    print(f'#{case+1} {max_res - min_res}')