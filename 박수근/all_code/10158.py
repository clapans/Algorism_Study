import sys

w,h = map(int,sys.stdin.readline().split())
x,y = map(int,sys.stdin.readline().split())
t = int(sys.stdin.readline())
cnt = 0
r_cnt = 0
dx,dy = 1,1
pre_x,pre_y = x + min(w-x,h-y), y + min(w-x,h-y)

while True:
    if x == pre_x and y == pre_y and r_cnt == 1 and dx == 1 and dy == 1:
        t = (t-cnt) % (cnt-1)
        cnt = 0
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
        if x == pre_x and y == pre_y and dx == 1 and dy == 1:
            r_cnt += 1
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