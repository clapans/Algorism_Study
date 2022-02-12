import sys

w,h = map(int,sys.stdin.readline().split())
x,y = map(int,sys.stdin.readline().split())
t = int(sys.stdin.readline())

tmp = min(w-x,h-y)
x,y = x+tmp,y+tmp
cnt = tmp
state = 1

while True:
    if cnt >= t:
        if state == 1:
            if x == w or y == h:
                print(x-(cnt-t),y-(cnt-t))
            else:
                print(x+(cnt-t),y+(cnt-t))
        else:
            if x == 0 or y == h:
                print(x+(cnt-t),y-(cnt-t))
            else:
                print(x-(cnt-t),y+(cnt-t))
        break
    else:
        state = -state
        if state == 1:
            if x == w or y == h:
                tmp = min(x,y)
                x,y = x-tmp,y-tmp
            else:
                tmp = min(w-x,h-y)
                x,y = x+tmp,y+tmp
        else:
            if x == 0 or y == h:
                tmp = min(w-x,y)
                x,y = x+tmp,y-tmp
            else:
                tmp = min(x,h-y)
                x,y = x-tmp,y+tmp
        cnt += tmp