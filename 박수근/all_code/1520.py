import sys

sys.setrecursionlimit(1000000)
a,b = map(int,sys.stdin.readline().split())
arr = []
visit = [[-1]*b for t in range(a)]
visit[0][0] = 1
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(a):
    arr.append(list(map(int,sys.stdin.readline().split())))

def dfs(x,y):
    if visit[x][y] != -1:
        return visit[x][y]
    visit[x][y] = 0
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < a and 0 <= new_y < b and arr[x][y] < arr[new_x][new_y]:
            visit[x][y] += dfs(new_x,new_y)
    return visit[x][y]

print(dfs(a-1,b-1))
