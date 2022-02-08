import sys

n = int(sys.stdin.readline())
members = []

res = []
def find_(x,visit):
    if sum(visit) == 7:
        tmp = [members[t] for t in range(n) if visit[t] == 1]
        if sum(tmp) == 100:
            res.append(sorted(tmp))
    else:
        for i in range(x+1,n):
            visit[i] = 1
            find_(i,visit)
            visit[i] = 0

for i in range(n):
    members.append(int(sys.stdin.readline()))

for i in range(n-7):
    tmp = [0] * n
    tmp[i] = 1
    find_(i,tmp)