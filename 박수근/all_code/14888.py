n = int(input())
operand = list(map(int,input().split()))
operator = list(map(int,input().split()))

def cal(x,y,oper):
    if oper == 0:
        return x + y
    elif oper == 1:
        return x - y
    elif oper == 2:
        return x * y
    else:
        if x > 0 and y > 0:
            return x // y
        x = - x
        return -int(x/y)

def calc(x,operator,sum_):
    if x == n-1:
        res.append(sum_)
    else:
        for i in range(4):
            if operator[i]:
                operator[i] -= 1
                tmp = cal(sum_,operand[x+1],i)
                calc(x+1,operator,tmp)
                operator[i] += 1

res = []
calc(0,operator,operand[0])
print(max(res))
print(min(res))