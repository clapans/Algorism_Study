import sys
sys.stdin = open('input.txt')
w,h = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
cnt=0

#(0,0)기준
def get(x,y):
    if x==1:
        return y+h
    elif x==2:
        return y
    elif x==3:
        return h-y
    else:
        return w+h-y

cor=[]
for _ in range(K+1):
    x, y = map(int, sys.stdin.readline().split())
    cor.append(get(x,y))

print(cor)



