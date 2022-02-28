import copy

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(v,cur_arr,r_cnt):
    global res
    if v == len(cores):
        if r_cnt > res[0]:
            res = [r_cnt,sum([t.count(1) for t in cur_arr])]
        elif r_cnt == res[0]:
            res = [r_cnt,min(res[1],sum([t.count(1) for t in cur_arr]))]
    else:
        arr_save = copy.deepcopy(cur_arr)
        x,y = cores[v]
        for t in range(4):
            cnt = 1
            while True:
                nx = x + cnt * dx[t]
                ny = y + cnt * dy[t]
                if 0 <= nx < n and 0 <= ny < n and cur_arr[nx][ny] == '0':
                    cur_arr[nx][ny] = 1
                else:
                    break
                cnt += 1
            if nx == -1 or ny == -1 or nx == n or ny == n:
                dfs(v+1,cur_arr,r_cnt+1)
            cur_arr = copy.deepcopy(arr_save)
        dfs(v+1,cur_arr,r_cnt)
        
for case in range(int(input())):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input().split())
    cores = []
    res = [0,0]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '1':
                if i == 0 or j == 0 or i == n-1 or j == n-1:
                    res[0] += 1
                else:
                    cores.append([i,j])
    dfs(0,arr,res[0])
    print(f'#{case+1} {res[1]}')