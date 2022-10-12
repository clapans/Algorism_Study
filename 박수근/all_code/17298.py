import sys

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
stack = []
nge = []

for num in nums[::-1]:
  tmp = -1
  while stack and stack[-1] <= num:
    stack.pop()
  if stack:
    tmp = stack[-1]
  nge.append(tmp) 
  stack.append(num)
  

  
print(*nge[::-1])

    
