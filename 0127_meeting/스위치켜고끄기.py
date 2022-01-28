import sys

n = int(sys.stdin.readline())
switch = list(map(int,sys.stdin.readline().split()))

student = int(sys.stdin.readline())

for i in range(student):
    gen,pos = map(int,sys.stdin.readline().split())
    if gen == 1:
        for t in range(pos-1,n,pos):
            switch[t] = 1 if switch[t] == 0 else 0
    else:
        switch[pos-1] = 1 if switch[pos-1] == 0 else 0
        cnt = 1
        while cnt <= min(pos-1,n-pos) and switch[pos-1-cnt] == switch[pos-1+cnt]:
            switch[pos-1-cnt] = 1 if switch[pos-1-cnt] == 0 else 0
            switch[pos-1+cnt] = 1 if switch[pos-1+cnt] == 0 else 0
            cnt += 1

for t in range(1,n+1):
    print(switch[t-1],end=' ')
    if t % 20 == 0:
        print('')