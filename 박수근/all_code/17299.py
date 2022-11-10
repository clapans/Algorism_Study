import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

num_dict = {}
stack = []
res = []

for t in arr:
    try:
        num_dict[t] += 1
    except:
        num_dict[t] = 1

for t in arr[::-1]:
    while stack and num_dict[stack[-1]] <= num_dict[t]:
        stack.pop()
    if stack:
        res.append(stack[-1])
    else:
        res.append(-1)
    stack.append(t)

for t in res[::-1]:
    print(t,end=' ')
