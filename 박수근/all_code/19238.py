import sys
from collections import deque
import heapq

dx = [1,-1,0,0]
dy = [0,0,1,-1]
n,m,fuel = map(int,sys.stdin.readline().split())
arr = []
customer = {}

for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

taxi = list(map(int,sys.stdin.readline().split()))
taxi[0] -= 1
taxi[1] -= 1

for _ in range(m):
    s1,s2,e1,e2 = map(int,sys.stdin.readline().split())
    customer[(s1-1,s2-1)] = [e1-1,e2-1]

def bfs():
    global fuel,taxi
    queue = deque([taxi])
    limit = int(1e9)
    candidate = []
    visit = [[-1]*n for _ in range(n)]
    visit[taxi[0]][taxi[1]] = 0
    while queue:
        node = queue.popleft()
        if visit[node[0]][node[1]] <= limit and visit[node[0]][node[1]] != -1:
            try:
                customer[(node[0],node[1])]
                heapq.heappush(candidate,(node[0],node[1]))
                limit = visit[node[0]][node[1]]
            except:
                for t in range(4):
                    nx = node[0] + dx[t]
                    ny = node[1] + dy[t]
                    if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == -1 and arr[nx][ny] == 0:
                        visit[nx][ny] = visit[node[0]][node[1]] + 1
                        queue.append([nx,ny])
    if not candidate:
        print(-1)
        quit(0)
    mini = heapq.heappop(candidate)
    desti = customer[mini]
    customer.pop(mini)
    fuel -= limit
    if fuel <= 0:
        print(-1)
        quit(0)
    queue.append(list(mini)+[0])
    visit = [[-1]*n for _ in range(n)]
    visit[mini[0]][mini[1]] = 1
    while queue:
        node = queue.popleft()
        if [node[0],node[1]] == desti:
            if fuel >= node[2]:
                fuel += node[2]
                taxi = desti
                return
            else:
                print(-1)
                quit(0)
        for t in range(4):
            nx = node[0] + dx[t]
            ny = node[1] + dy[t]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == -1 and arr[nx][ny] == 0:
                visit[nx][ny] = 1
                queue.append([nx,ny,node[2]+1])
    print(-1)
    quit(0)

while True:
    bfs()
    if not customer:
        print(fuel)
        break