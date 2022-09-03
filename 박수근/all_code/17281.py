import sys
import itertools
from collections import deque

n = int(sys.stdin.readline())
arr = []
score = 0

for _ in range(n):
    arr.append(sys.stdin.readline().split())

def getScore(base):
    tmp = 0
    while len(base) > 3:
        if base.popleft() == 1:
            tmp += 1
    return [tmp,base]

def play(batOrder):
    num = 0
    tmp = 0
    for t in range(n):
        cnt = 0
        base = deque([])
        while cnt < 3:
            batter = batOrder[num]
            if arr[t][batter] == '0':
                cnt += 1
            elif arr[t][batter] == '1':
                base.append(1)
            elif arr[t][batter] == '2':
                base += [1,0]
            elif arr[t][batter] == '3':
                base += [1,0,0]
            else:
                base += [1,0,0,0]
            num = num + 1 if num < 8 else 0
            res = getScore(base)
            tmp += res[0]
            base = deque([t for t in res[1]])
    return tmp
        
for case in itertools.permutations(range(1,9)):
    new_case = list(case[:3]) + [0] + list(case[3:])
    score = max(score,play(new_case))
    
print(score)