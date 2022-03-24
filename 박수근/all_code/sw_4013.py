def rotate(x,y):
    if y == -1:
        magnet[x] = magnet[x][1:] + [magnet[x][0]]
    else:
        magnet[x] = [magnet[x][-1]] + magnet[x][:-1]

for case in range(int(input())):
    k = int(input())
    magnet = []
    for _ in range(4):
        magnet.append(list(map(int,input().split())))
    
    for _ in range(k):
        a,b = map(int,input().split())
        tmp = b
        wait = [[a-1,b]]
        for i in range(a-1,3):
            if magnet[i][2] != magnet[i+1][-2]:
                tmp = -tmp
                wait.append([i+1,tmp])
            else:
                break
        tmp = b
        for i in range(a-1,0,-1):
            if magnet[i][-2] != magnet[i-1][2]:
                tmp = -tmp
                wait.append([i-1,tmp])
            else:
                break
        for i in wait:
            rotate(*i)

    res = 0
    for i in range(4):
        if magnet[i][0]:
            res += 2**i
    print(f'#{case+1} {res}')