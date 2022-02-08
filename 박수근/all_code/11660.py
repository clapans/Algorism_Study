import sys

n,m = map(int,sys.stdin.readline().split())

arr = [[0]*(n+1)]
tmp = [0] + list(map(int,sys.stdin.readline().split()))
arr.append([sum(tmp[:t+1]) for t in range(len(tmp))])

for i in range(n-1):
    tmp = [0] + list(map(int,sys.stdin.readline().split()))
    s = [sum(tmp[:t+1]) for t in range(len(tmp))]
    arr.append(list(map(lambda x : x[0]+x[1],zip(arr[-1],s))))


for i in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    print(arr[x2][y2] - arr[x2][y1-1] - arr[x1-1][y2] + arr[x1-1][y1-1])

