import sys
import pprint
res = set([])

for i in range(4):
    a,b,c,d, = map(int,sys.stdin.readline().split())
    for x in range(a,c):
        for y in range(b,d):
            res.add(tuple[x,y])

pprint.pprint(res)


'''
import sys

rectangle = [[] for t in range(4)]

for i in range(4):
    a,b,c,d, = map(int,sys.stdin.readline().split())
    for x in range(a,c):
        for y in range(b,d):
            rectangle[i].append([x,y])
    rectangle[i] = set([tuple(t) for t in rectangle[i]])

res = set([])

for i in range(4):
    res = res | rectangle[i]

print(len(res))'''

