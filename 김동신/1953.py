from pprint import pprint
# 상 하 좌 우
deltas = [[-1,0],[1,0],[0,-1],[0,1]]
cant_connection = {
    "0":[3,4,7],
    "1":[3,5,6],
    "2":[2,6,7],
    "3":[2,4,5]
}

search_loc = {
    "1":deltas[:],
    "2":[deltas[0],deltas[1]],
    "3":[deltas[2],deltas[3]],
    "4":[deltas[0],deltas[3]],
    "5":[deltas[1],deltas[3]],
    "6":[deltas[1],deltas[2]],
    "7":[deltas[0],deltas[2]]
}


first = list(map(int,input().split()))
N = first[0]
M = first[1]
hole = first[2],first[3]
time = first[4]

arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

# 맨홀 위치 = 시작점

queue = [[hole[0],hole[1]]]
visited[hole[0]][hole[1]] = 1
for _ in range(time) :
    imsi = []
    while queue :
        tmp=queue.pop(0)
        x = tmp[0]
        y = tmp[1]
        hole_loc = arr[x][y]

        for delta in search_loc[str(hole_loc)] :
            direction = deltas.index(delta)
            nx = x + delta[0]
            ny = y + delta[1]
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] and visited[nx][ny] == 0:
                # 연결 조건
                if arr[nx][ny] in cant_connection[str(direction)] :
                    continue
                visited[nx][ny] = 1
                imsi.append([nx,ny])
    queue = imsi[:]

    cnt=0
    for i in range(N) :
        for j in range(M) :
            if visited[i][j] :
                cnt+=1
    print(f'# {cnt}')