import sys
for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, sys.stdin.readline().split(" "))


    xt = max(x1,x2)
    pt = min(p1,p2)
    yt = max(y1,y2)
    qt = min(q1,q2)

    tt=pt-xt
    yy=qt-yt


    if tt>0 and yy>0:
        print('a')
    elif tt<0 or yy<0:
        print('d')
    elif tt==0 and yy==0:
        print('c')
    else:
        print('b')