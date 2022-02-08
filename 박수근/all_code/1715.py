import heapq
import sys

n = int(input())
num = list(map(int,input().split()))
nums = []
cnt = 1

for i in num:
    heapq.heappush(nums,i)

for t in range(5):
    print(nums)
    tmp = heapq.heappop(nums)
    if tmp <= cnt:
        cnt += 1
        leng = len(nums)
        for i in range(leng):
            heapq.heappush(nums,nums[i] + tmp)
    else:
        print(cnt)
        break


