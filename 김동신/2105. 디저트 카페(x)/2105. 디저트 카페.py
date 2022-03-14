import sys
sys.stdin = open("input.txt")

T = int(input())

delta = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
can_delta = {
    0 : [[1,1],[1,-1]],
    1 : [[1,-1],[-1,-1]],
    2 : [[-1,-1],[-1,1]],
    3 : [[-1,1],[1,1]],
}
def dfs(N,arr,d,stack,visited) :
    global delta
    global can_delta
    while True:
        loc = stack[-1]
        for dx,dy in can_delta[d] :
            x = loc[0] + dx
            y = loc[1] + dy
            if 0 <= x < N and 0 <= y < N and arr[x][y] not in menu and visited[x][y] == 0:
                menu.append(arr[x][y])
                visited[x][y] = -1
                stack.append([x,y])
                dfs(N,arr,d,stack,visited)
            else:
                if d % 4 == 3 and [x,y] == [i,j]:
                    return len(menu)
                elif d == 3 :
                    return -1
                else:
                    d += 1

for tc in range(T):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]
    res = 0
    for i in range(N) :
        for j in range(N) :
            visited = [[0] * N for _ in range(N)]
            menu = []
            stack = []
            menu.append(arr[i][j])
            visited[i][j] = -1
            stack.append([i, j])
            d = 0
            tmp = dfs(N, arr,d,stack,visited)
            if res < tmp :
                res = tmp

    print(f'#{tc+1} {res}')






