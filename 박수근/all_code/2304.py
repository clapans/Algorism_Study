import sys

n = int(sys.stdin.readline())
graph = [0] * 1001

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    graph[a] = b

def roof(graph):
    res = 0
    h = 0
    for i in graph:
        if i == max(graph):
            break
        h = max(h,i)
        res += h
    return res

max_ = max(graph)
res = max_ * (abs(graph.index(max_) - (1001 - graph[::-1].index(max_))))
res += roof(graph)
res += roof(graph[::-1])

print(res)