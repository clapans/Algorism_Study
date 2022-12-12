n,m,h = map(int,input().split())
arr = [[0]*(n+1) for _ in range(h+1)]
case = []

for _ in range(m):
    a,b = map(int,input().split())
    arr[a][b] = 1

def isCheck():
    for i in range(1,n+1):
        if i != ladder(i):
            return False
    return True

def ladder(x):
    cnt = 1
    while cnt < h + 1:
        if arr[cnt][x]:
            x += 1
        elif arr[cnt][x-1]:
            x -= 1
        cnt += 1
    return x

def combination(a,b,candidate,cnt):
    global case
    if cnt == len(candidate):
        case.append(candidate[:])
    elif a < h + 1:
        if arr[a][b-1] == 0 and arr[a][b] == 0:
            candidate.append([a,b])
            if b + 1 < n:
                combination(a,b+1,candidate,cnt)
            elif a < h + 1:
                combination(a+1,1,candidate,cnt)
            candidate.pop()
        if b + 1 < n:
            combination(a,b+1,candidate,cnt)
        elif a < h + 1:
            combination(a+1,1,candidate,cnt)

def fraud():
    if isCheck():
        return 0
    for i in range(1,4):
        combination(1,1,[],i)
        for cand in case:
            for t in cand:
                arr[t[0]][t[1]] = 1
            if isCheck():
                return i
            for t in cand:
                arr[t[0]][t[1]] = 0
    return -1

print(fraud())