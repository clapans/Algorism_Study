import sys

w,h = map(int,sys.stdin.readline().split())
p,q = map(int,sys.stdin.readline().split())
t = int(sys.stdin.readline())

cnt = 0
dx,dy = 1,1
pre_p,pre_q = p,q
if 0 <= w+q-p <= h and pre_p != w:
    p,q = w,w+q-p
    dx = -dx
if 0 <= h+p-q <= w and pre_q != h:
    p,q = h+p-q,h
    dy = -dy
cnt += min(abs(pre_p-p),abs(pre_q-q))

while True:
    if cnt >= t:
        if p == 0 or p == h:
            dy = -dy
        else:
            dx = -dx
        for v in range(cnt-t):
            p += dx
            q += dy
        print(p,q)
        break
    else:
        if dx * dy == 1:
            pre_p,pre_q = p,q
            if 0 <= w+q-p <= h and pre_p != w:
                p,q = w,w+q-p
                dx = -dx
            elif 0 <= h+p-q <= w and pre_q != h:
                p,q = h+p-q,h
                dy = -dy
            elif 0 <= p-q <= w and pre_q != 0:
                p,q = p-q,0
                dy = -dy
            else:
                p,q = 0,q-p
                dx = -dx
            cnt += min(abs(pre_p-p),abs(pre_q-q))
        else:
            pre_p,pre_q = p,q
            if 0 <= p+q < h and pre_p != 0:
                p,q = 0,p+q
                dx = -dx
            elif 0 <= p+q < w and pre_q != 0:
                p,q = p+q,0
                dy = -dy
            elif 0 <= p+q-w < h and pre_p != w:
                p,q = w,p+q-w
                dx = -dx
            else:
                p,q = p+q-h,h
                dy = -dy
            cnt += min(abs(pre_p-p),abs(pre_q-q))