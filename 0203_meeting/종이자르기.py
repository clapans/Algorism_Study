import sys

a,b = map(int,sys.stdin.readline().split())

w,h = [0,a],[0,b]

for i in range(int(sys.stdin.readline())):
    m,n = map(int,sys.stdin.readline().split())
    if m == 1:
        w.append(n)
    else:
        h.append(n)

width = 0
height = 0
w.sort()
h.sort()

for i in range(len(w)-1):
    width = max(width,w[i+1] - w[i])

for i in range(len(h)-1):
    height = max(height,h[i+1] - h[i])

print(width * height)

