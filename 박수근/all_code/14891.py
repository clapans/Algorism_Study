import sys
from collections import deque

wheel = []

def rot_(num,rot):
    visit[num] = 1
    left = wheel[num][6]
    right = wheel[num][2]
    wheel[num].rotate(rot)
    if num + 1 < 5:
        if right != wheel[num+1][6] and visit[num+1] == 0:
            rot_(num+1,-rot)
    if num - 1 > 0:
        if left != wheel[num-1][2] and visit[num-1] == 0:
            rot_(num-1,-rot)

wheel.append(deque([]))
for i in range(4):
    wheel.append(deque(list(sys.stdin.readline().rstrip())))

for i in range(int(sys.stdin.readline())):
    num,rot = map(int,sys.stdin.readline().split())
    visit = [0,0,0,0,0]
    rot_(num,rot)

print(sum([2**(t-1) for t in range(1,5) if wheel[t][0] == '1']))

print(wheel)

