import sys

n = int(input())
order = list(map(int,sys.stdin.readline().split()))
lst = []

for t in range(n):
    lst = lst[:t-order[t]] + [t+1] + lst[t-order[t]:]

print(*lst)