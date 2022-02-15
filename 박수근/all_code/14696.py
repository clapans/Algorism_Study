import sys

def fight():
    for t in range(len(a)):
        if a[t] > b[t]:
            return 'A'
        elif a[t] == b[t]:
            pass
        else:
            return 'B'
    return 'D'

for case in range(int(sys.stdin.readline())):
    a = sorted(list(map(int,sys.stdin.readline().split()))[1:],reverse=True)
    b = sorted(list(map(int,sys.stdin.readline().split()))[1:],reverse=True)
    while len(a) != len(b):
        if len(a) < len(b):
            a.append(0)
        else:
            b.append(0)

    print(fight())