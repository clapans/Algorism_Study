import sys
import copy

n = int(sys.stdin.readline())

def up(m):
    for i in range(n):
        res = []
        tmp = 0
        for j in range(n):
            if tmp == 0:
                tmp = m[j][i]
            else:
                if m[j][i] == 0:
                    continue
                if tmp == m[j][i]:
                    tmp += m[j][i]
                    res.append(tmp)
                    tmp = 0
                else:
                    res.append(tmp)
                    tmp = m[j][i]
        res.append(tmp)
        while len(res) < n:
            res.append(0)
        for x in range(n):
            m[x][i] = res[x]
    return m

def down(m):
    for i in range(n):
        res = []
        tmp = 0
        for j in range(n-1,-1,-1):
            if tmp == 0:
                tmp = m[j][i]
            else:
                if m[j][i] == 0:
                    continue
                if tmp == m[j][i]:
                    tmp += m[j][i]
                    res.append(tmp)
                    tmp = 0
                else:
                    res.append(tmp)
                    tmp = m[j][i]
        res.append(tmp)
        while len(res) < n:
            res.append(0)
        res = res[::-1]
        for x in range(n):
            m[x][i] = res[x]
    return m

def left(m):
    for i in range(n):
        res = []
        tmp = 0
        for j in range(n):
            if tmp == 0:
                tmp = m[i][j]
            else:
                if m[i][j] == 0:
                    continue
                if tmp == m[i][j]:
                    tmp += m[i][j]
                    res.append(tmp)
                    tmp = 0
                else:
                    res.append(tmp)
                    tmp = m[i][j]
        res.append(tmp)
        while len(res) < n:
            res.append(0)
        for x in range(n):
            m[i][x] = res[x]
    return m

def right(m):
    for i in range(n):
        res = []
        tmp = 0
        for j in range(n-1,-1,-1):
            if tmp == 0:
                tmp = m[i][j]
            else:
                if m[i][j] == 0:
                    continue
                if tmp == m[i][j]:
                    tmp += m[i][j]
                    res.append(tmp)
                    tmp = 0
                else:
                    res.append(tmp)
                    tmp = m[i][j]
        res.append(tmp)
        while len(res) < n:
            res.append(0)
        res = res[::-1]
        for x in range(n):
            m[i][x] = res[x]
    return m
res = 0
def dfs(cnt,lst):
    global res
    if cnt == 5:
        for t in range(n):
            res = max(res,max(lst[t]))         
    else:
        save = copy.deepcopy(lst)
        for i in range(4):
            if i == 0:
                dfs(cnt+1,left(copy.deepcopy(save)))
            elif i == 1:
                dfs(cnt+1,right(copy.deepcopy(save)))
            elif i == 2:
                dfs(cnt+1,up(copy.deepcopy(save)))
            else:
                dfs(cnt+1,down(copy.deepcopy(save)))

arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

dfs(0,copy.deepcopy(arr))
print(res)

