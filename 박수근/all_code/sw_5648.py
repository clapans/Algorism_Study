dx = [0,0,-1,1]
dy = [1,-1,0,0]

for case in range(int(input())):
    n = int(input())
    atom = []
    for _ in range(n):
        atom.append(list(map(int,input().split())))
    res = 0
    while atom:
        tmp = {}
        for t in atom:
            nx = t[0] + 0.5*dx[t[2]]
            ny = t[1] + 0.5*dy[t[2]]
            if -1000 <= nx <= 1000 and -1000 <= ny <= 1000:
                try:
                    tmp[(nx,ny)].append(t)
                except:
                    tmp[(nx,ny)] = [t]

        new = []
        for k,v in tmp.items():
            if len(v) == 1:
                new.append(v[0])
            else:
                for i in v:
                    res += i[3]
        atom = new[:]

    print(f'#{case+1} {res}')