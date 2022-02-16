import sys
sys.stdin = open('input.txt')
w,h = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
lst1=[]
lst2=[]
lst3=[]
lst4=[]
std=[0]*2
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    if x==1:
        lst1.append(y)
    elif x==2:
        lst2.append(y)
    elif x==3:
        lst3.append(y)
    else:
        lst4.append(y)

print(lst1,lst2,lst3,lst4)
x, y = map(int, sys.stdin.readline().split())
std[0]=x
std[1]=y
cnt=0
if std[0]==2:
    cnt+=abs(std[1]-lst2[0])+(lst1[0]+h)

print(std)




