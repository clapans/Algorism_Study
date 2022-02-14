import sys

w,h = map(int,sys.stdin.readline().split())
x,y = map(int,sys.stdin.readline().split())
t = int(sys.stdin.readline())

x_axis = [v for v in range(x,w)] + [v for v in range(w,0,-1)] + [v for v in range(x)]
y_axis = [v for v in range(y,h)] + [v for v in range(h,0,-1)] + [v for v in range(y)] 

print(x_axis[t % len(x_axis)],y_axis[t % len(y_axis)])