import sys

n = int(sys.stdin.readline())
pos = list(map(int,sys.stdin.readline().split()))
sort_pos =sorted(set(pos))
pos_dic = {}

for i in range(len(sort_pos)):
    pos_dic[sort_pos[i]] = i

for i in pos:
    print(pos_dic[i],end=' ')