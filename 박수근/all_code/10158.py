import sys

w,h = map(int,sys.stdin.readline().split())
x,y = map(int,sys.stdin.readline().split())
t = int(sys.stdin.readline())
cnt = 0
dx,dy = 1,1

while True:
    if cnt >= t:
        if dx * dy == 1:
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
        dx = -dx if x == 0 or x == w else dx
        dy = -dy if y == 0 or y == h else dy
        if dx == 1 and dy == 1:
            tmp = min(w-x,h-y)
        elif dx == 1 and dy == -1:
            tmp = min(w-x,y)
        elif dx == -1 and dy == 1:
            tmp = min(x,h-y)
        else:
            tmp = min(x,y)
        cnt += tmp
        x += dx*tmp
        y += dy*tmp