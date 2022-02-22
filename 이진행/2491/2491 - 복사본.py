



N = int(input())
K = list(map(int, input().split()))

cnt = 1
max_1 = 1

for a in range(1,N):
    if K[a]>=K[a-1]:
        cnt+=1
    else:
        cnt=1
    if max_1 < cnt:
        max_1 = cnt

for a in range(1,N):
    if K[a] <=K[a-1]:
        cnt+=1
    else:
        cnt=1
    if max_1 < cnt:
        max_1 = cnt
print(max_1)


