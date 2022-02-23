def i(x,lst):
    pw = pw[:x+1] + lst + pw[x+1:]

def d(x,cnt):
    pw = pw[:x+1] + pw[x+cnt+1:]

def a(x,lst):
    pw += lst

for case in range(10):
    n = int(input())
    pw = list(map(int,input().split()))
    cmd = int(input())
    cmds = list(input())
    tmp = []
    for t in cmds:
        if t == 'I':
            i(int(tmp[0]),list(map(int,tmp[2:])))
            tmp = []
        elif t == 'D':
            d(int(tmp[0]),int(tmp[1]))
            tmp = []
        elif t == 'A':
            a(int(tmp[0]),list(map(int,tmp[2:])))
            tmp = []
        else:
            tmp.append(t)
    print(f'#{case+1}',end=' ')
    print(*cmds[:10])
