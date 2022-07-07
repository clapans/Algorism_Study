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
    while True:
        if minus and isCheck(num+cnt):
            return cnt + len(str(num+cnt))
        if plus and isCheck(num-cnt): 
            return cnt + len(str(num-cnt))
        cnt += 1

def isNum():
    cnt = 0
    for t in broke:
        if t != "+" or t != "-":
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
if plus and n <= 100:
    distance = min(distance,100-n)
if minus and n >= 100:
    distance = min(distance,n-100)
    
if isNum() == 10:
    print(abs(n-100))
else:
    print(min(abs(n-100),closest(n)))