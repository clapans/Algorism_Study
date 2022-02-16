import sys
sys.stdin = open('input.txt')
N,K = map(int, sys.stdin.readline().split())

list_1=[0]*1000
list_0=[0]*1000

for _ in range(N):
    S,Y = map(int, sys.stdin.readline().split())
    if S == 0:
        list_0[Y] +=1
    if S == 1:
        list_1[Y] +=1

#학년 탐색
for j in range(1,7):
    #여자
    if list_0[j] % K==0:
        list_0[j] = list_0[j] // K
    else:
        list_0[j] = (list_0[j]//K)+1
    #남자
    if list_1[j] % K == 0:
        list_1[j] = list_1[j] // K
    else:
        list_1[j] = (list_1[j] // K) + 1

print(sum(list_0)+sum(list_1))


