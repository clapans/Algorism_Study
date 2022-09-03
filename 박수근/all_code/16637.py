import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

res = -(2**31)

def cal(a,b):
    tmp = s[a:b+1]
    s_ = int(tmp[0])
    for i in range(1,len(tmp),2):
        if tmp[i] == '+':
            s_ += int(tmp[i+1])
        elif tmp[i] == '-':
            s_ -= int(tmp[i+1])
        else:
            s_ *= int(tmp[i+1])
    return s_
        
def dfs(x,operand):
    global res
    if x < len(s):
        if x == 0:
            operand.append(0)
            dfs(x+2,operand)
            operand.pop()
        else:
            operand.append(x)
            dfs(x+2,operand)
            operand.pop()
            if len(operand) > 1 and operand[-1] - operand[-2] < 4: 
                tmp = operand[-1] 
                operand[-1] = x
                dfs(x+2,operand)
                operand[-1] = tmp
    else:
        score = cal(0,operand[0])
        pre = int(operand[0])+2
        operator = operand[0] + 1
        for i in range(1,len(operand)):
            oper = cal(pre,operand[i])
            if s[operator] == '+':
                score += oper
            elif s[operator] == '-':
                score -= oper
            else:
                score *= oper
            pre = int(operand[i])+2
            operator = operand[i] + 1
        res = max(res,score)

dfs(0,[])
print(res)