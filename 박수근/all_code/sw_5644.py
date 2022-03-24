dx = [0,-1,0,1,0]
dy = [0,0,1,0,-1]

def distance(x,y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

for case in range(int(input())):
    m,a = map(int,input().split())
    route = []
    for _ in range(2):
        route.append(list(map(int,input().split())))
    
    ap = []
    for _ in range(a):
        tmp = list(map(int,input().split()))
        ap.append([tmp[1]-1,tmp[0]-1,tmp[2],tmp[3]])
    
    cnt = 0
    pos_a,pos_b = [0,0],[9,9]
    res = 0
    while cnt <= m:
        a_able,b_able = [],[]
        for t in range(a):
            if distance(ap[t][:2],pos_a) <= ap[t][2]:
                a_able.append([ap[t][3],t])
            if distance(ap[t][:2],pos_b) <= ap[t][2]:
                b_able.append([ap[t][3],t])
        a_able = sorted(a_able,key=lambda x : x[0])
        b_able = sorted(b_able,key=lambda x : x[0])
        a_tmp,b_tmp = 0,0
        if a_able and b_able:
            at = a_able.pop()
            bt = b_able.pop()
            if at == bt:
                a_n,b_n = 0,0
                if a_able:
                    a_n = a_able.pop()[0]
                if b_able:
                    b_n = b_able.pop()[0]
                res += at[0] + max(a_n,b_n)
            else:
                res += at[0] + bt[0]
        else:
            if a_able:
                res += a_able.pop()[0]
            if b_able:
                res += b_able.pop()[0]
        if cnt == m:
            break
        pos_a = [pos_a[0] + dx[route[0][cnt]], pos_a[1] + dy[route[0][cnt]]]
        pos_b = [pos_b[0] + dx[route[1][cnt]], pos_b[1] + dy[route[1][cnt]]]
        cnt += 1
    
    print(f'#{case+1} {res}')
