import sys

def synergy(lst):
    total = 0
    for i in lst:
        for j in lst:
            if i != j:
                total += arr[i][j]
    return total

def dfs(x):
    global res
    if x == n:
        res = min(res,abs(synergy(home) - synergy(away)))
    else:
        if len(home) < n//2:
            home.append(x)
            dfs(x+1)
            home.pop()
        if len(away) < n//2:
            away.append(x)
            dfs(x+1)
            away.pop()

n = int(sys.stdin.readline())
arr = []
res = int(1e9)

for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

home,away = [],[]
dfs(0)
print(res)