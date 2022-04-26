import sys
from collections import deque

arr = ""
for _ in range(3):
    arr += sys.stdin.readline().strip().replace(' ','')

dx = [1,-1,0,0]
dy = [0,0,1,-1]

answer = "123456780"
visit = {}
visit[arr] = 0
queue = deque([arr])
while queue:
    puzzle = queue.popleft()
    if puzzle == answer:
        print(visit[puzzle])
        quit(0)
    idx = puzzle.index("0")
    start = [idx//3,idx%3]
    for t in range(4):
        nx = start[0] + dx[t]
        ny = start[1] + dy[t]
        if 0 <= nx < 3 and 0 <= ny < 3:
            n_puzzle = ""
            tmp = puzzle[3*nx + ny]
            for i in range(9):
                if i != 3*nx+ny and i != idx:
                    n_puzzle += puzzle[i]
                elif i == 3*nx+ny:
                    n_puzzle += "0"
                else:
                    n_puzzle += tmp
            try:
                visit[n_puzzle]
            except:
                visit[n_puzzle] = visit[puzzle] + 1
                queue.append(n_puzzle)
            
print(-1)