import sys

cnt,e,w,s,n = map(int,sys.stdin.readline().split())
arr = [[0]*(2*cnt+1) for _ in range(2*cnt+1)]
visit = [[0]*(2*cnt+1) for _ in range(2*cnt+1)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
percent = [e/100,w/100,s/100,n/100]

simpleCase = 0

def dfs(x,y,v,per):
    global simpleCase
    if v == cnt:
        simpleCase += per
    else:
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < 2*cnt+1 and 0 <= ny < 2*cnt+1:
                if visit[nx][ny] == 1:
                    continue
                visit[nx][ny] = 1
                dfs(nx,ny,v+1,per*percent[t])
                visit[nx][ny] = 0

visit[cnt][cnt] = 1
dfs(cnt,cnt,0,1)
print(simpleCase)