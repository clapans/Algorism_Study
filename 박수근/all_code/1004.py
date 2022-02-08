import sys

for case in range(int(sys.stdin.readline())):
    res = 0
    prince,rose = [0,0],[0,0]
    prince[0],prince[1],rose[0],rose[1] = map(int,sys.stdin.readline().split())
    for planet in range(int(sys.stdin.readline())):
        x,y,r = map(int,sys.stdin.readline().split())
        cnt = 0
        for t in [prince,rose]:
            if pow(t[0]-x,2)+pow(t[1]-y,2) <= pow(r,2):
                cnt += 1
        if cnt == 1:
            res += 1
    print(res)