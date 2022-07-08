import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

def isCheck(num):
    for t in str(num):
        if t in broke:
            return False
    return True

def closest(num):
    cnt = 0
    tmp = [int(1e9),int(1e9)]
    while minus:
        if isCheck(num+cnt):
            tmp[0] = cnt + len(str(num+cnt))
            break
        cnt += 1
    cnt = 0
    while plus:
        if num-cnt < 0:
            break
        if isCheck(num-cnt): 
            tmp[1] = cnt + len(str(num-cnt))
            break
        cnt += 1
    return min(tmp)

def isNum():
    cnt = 0
    for t in broke:
        if t != "+" and t != "-":
            cnt += 1
    return cnt

plus,minus = True,True
broke = []
if m > 0:
    broke = sys.stdin.readline().split()
    if "+" in broke:
        plus = False
    if "-" in broke:
        minus = False

distance = int(1e9)
if minus and n <= 100:
    distance = min(distance,100-n)
if plus and n >= 100:
    distance = min(distance,n-100)

if isNum() == 10:
    print(distance)
else:
    print(min(distance,closest(n)))