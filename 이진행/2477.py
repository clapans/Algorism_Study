import sys

m = int(sys.stdin.readline())
tool=[]
for _ in range(6):
    x, y = map(int, sys.stdin.readline().split(" "))
    tool.append(y)

big = 0
small = 0

for x in range(6):
    tmp = tool[x] * tool[(x+1)%6]
    if big < tmp:
        big = tmp
        idx = x
        
small = tool[(idx+3)%6] * tool[(idx+4)%6]
print(m*(big-small))


# m = int(input())
# tool=[]
# for _ in range(6):
#     x, y =map(int, input().split(" "))
#     tool.append(y)

# big = 0
# small = 0
# for x in range(6):
#     tmp = tool[x]*tool[(x+1)&6]
#     if big <tmp:
#         big = tmp
#         idx = x

# small = tool[(x+3)%6]*tool[(x+4)%6]
# print(m*(big-small))
