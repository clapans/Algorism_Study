import sys

n = int(sys.stdin.readline())
members = []

for i in range(9):
    members.append(int(sys.stdin.readline()))

def find():
    for i in range(9):
        for j in range(i+1,9):
            tmp = [members[t] for t in range(9) if t not in [i,j]]
            if sum(tmp) == 100:
                return sorted(tmp)
    return 0

for i in find():
    print(i)


