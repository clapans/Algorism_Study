import sys
from collections import deque

a,b = map(int,sys.stdin.readline().split())
lst = deque(list(map(int,sys.stdin.readline().split())))
queue = deque([t for t in range(1,a+1)])
cnt = 0

while lst:
    if queue[0] == lst[0]:
        queue.popleft()
        lst.popleft()
    else:
        tmp = queue.index(lst[0])
        if tmp < len(queue) - tmp:
            for i in range(tmp):
                queue.rotate(-1)
                cnt += 1
        else:
            for i in range(len(queue)-tmp):
                queue.rotate(1)
                cnt += 1

print(cnt)