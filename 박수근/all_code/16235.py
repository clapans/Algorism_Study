import sys
import heapq

def spring():
    global tree
    dead = []
    older = []
    for age,v in tree.items():
        for t in v:
            if age <= arr[t[0]][t[1]]:
                arr[t[0]][t[1]] -= age
                v.remove(t)
                older.append([t[0],t[1],age + 1])
            else:
                dead.append(t)
    for t in older:
        try:
            tree[t[2]].append([t[0],t[1]])
        except:
            tree[t[2]] = [[t[0],t[1]]]

    return dead

def summer(dead):
    for t in dead:
        arr[t[0]][t[1]] += t[2] // 2
    
def autumn():
    global tree
    addTree = []
    for t in tree[]
    for t in addTree:
        heapq.heappush(tree,t)

def winter():
    for i in range(N):
        for j in range(N):
            arr[i][j] += food[i][j]

N,M,K = map(int,sys.stdin.readline().split())
arr = [[5]*N for _ in range(N)]

food = []
tree = {}

for _ in range(N):
    food.append(list(map(int,sys.stdin.readline().split())))

for _ in range(M):
    x,y,age = map(int,sys.stdin.readline().split())
    try:
        tree[age].append([x-1,y-1])
    except:
        tree[age] = [[x-1,y-1]]

dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,-1,1,1,-1]

cnt = 0

while cnt < K:
    dead = spring()
    summer(dead)
    autumn()
    winter()
    cnt += 1

print(len(tree))