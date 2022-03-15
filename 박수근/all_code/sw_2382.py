dx = [-1,1,0,0]
dy = [0,0,-1,1]
dir_dict = {1: 2, 2: 1, 3: 4, 4: 3}

for case in range(int(input())):
    n,m,k = map(int,input().split())
    bugs = []
    for _ in range(k):
        bugs.append(list(map(int,input().split())))
    cnt = 0
    while cnt < m:
        tmp = []
        for t in bugs:
            nx = t[0] + dx[t[3]-1]
            ny = t[1] + dy[t[3]-1]
            nx,ny = min(n-1,nx),min(n-1,ny)
            nx,ny = max(0,nx),max(0,ny)
            n_num,nd = t[2],t[3]
            if nx == 0 or nx == n-1 or ny == 0 or ny == n-1:
                nd = dir_dict[t[3]]
                n_num = t[2]//2     
            for v in range(len(tmp)):
                if tmp[v][:2] == [nx,ny]:
                    try:
                        tmp[v][3] = nd if n_num > tmp[v][4] else tmp[v][3]
                        tmp[v][4] = max(tmp[v][4],n_num)
                    except:
                        tmp[v][3] = nd if n_num > tmp[v][2] else tmp[v][3]
                        tmp[v].append(max(tmp[v][2],n_num))
                    tmp[v][2] += n_num
                    break
            else:
                if n_num:
                    tmp.append([nx,ny,n_num,nd])
        bugs = tmp[:]
        cnt += 1
    print(f'#{case+1} {sum([t[2] for t in bugs])}')