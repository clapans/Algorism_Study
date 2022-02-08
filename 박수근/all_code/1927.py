import heapq
import sys

def prin_t():
    try:
        return heapq.heappop(nums)
    except:
        return 0

def push_(x):
    heapq.heappush(nums,x)


N = int(input())
nums = []

for i in range(N):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        print(prin_t())
    else:
        push_(tmp)
