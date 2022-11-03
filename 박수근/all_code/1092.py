import sys

n = int(sys.stdin.readline())
crane = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))
box.sort(reverse=True)
crane.sort(reverse=True)

cnt = 1
idx = 0
idx2 = 0
tmp = []
alreadyDict = {}
doneCnt = 0

if crane[idx] < box[0]:
    print(-1)
    quit()

while True:
    idx = 0
    idx2 = 0

    while True:
        try:
            alreadyDict[idx2]
        except:
            if box[idx2] <= crane[idx]:
                idx += 1
                alreadyDict[idx2] = 1
                doneCnt += 1
                if idx == n:
                    break
        idx2 += 1
        if idx2 == m:
            break
        
    if doneCnt == m:
        break
    cnt += 1

print(cnt)