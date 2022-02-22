import sys

n = int(sys.stdin.readline())
paper = set()

for t in range(n):
    a,b = map(int,sys.stdin.readline().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            paper.add((i,j))

print(len(paper))