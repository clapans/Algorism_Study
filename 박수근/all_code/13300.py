import sys

n,k = map(int,sys.stdin.readline().split())
class_ = [[0,0,0,0,0,0] for t in range(2)]
res = 0

for t in range(n):
    s,y = map(int,sys.stdin.readline().split())
    class_[s][y-1] += 1

for i in range(2):
    for j in range(6):
        res += (class_[i][j]) // k
        if class_[i][j] % k:
            res += 1

print(res) 