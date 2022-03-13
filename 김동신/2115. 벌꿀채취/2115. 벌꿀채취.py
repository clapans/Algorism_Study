import sys
sys.stdin = open("input.txt")
def honey(N,M,C):
    global arr
    res=0
    for i in range(N) :
        for j in range(N-(M-1)) :
            total=[]
            for m in range(M) :
                total.append(arr[i][j+m])
            if -1 in total :
                continue

            tmp = 0

            if sum(total) <= C :
                for each in total :
                    tmp += each**2

            else :
                for ti in range(1<<len(total)) :
                    powerset=[]
                    maximum = 0
                    for tj in range(len(total)) :
                        if ti & (1<<tj) :
                            powerset.append(total[tj])
                    if sum(powerset) > C :
                        continue
                    else :
                        for each in powerset :
                            maximum += each**2
                        if maximum > tmp :
                            tmp = maximum

                # while len(total) :
                #     if maximum + max(total) > C :
                #         total.remove(max(total))
                #     else :
                #         maximum += max(total)
                #         tmps.append(max(total))
                #         total.remove(max(total))
                #
                # for each in tmps :
                #     tmp += each**2
            if res < tmp:
                res = tmp
                loc = []
                for m in range(M):
                    loc.append([i,j+m])
    for x,y in loc :
        arr[x][y] = -1

    return res

# N,M,C = 3, 3, 10
# arr = [[7,2,9],[6,6,6],[5,5,7]]
# print(arr)
# worker1 = honey(N,M,C)
# print(worker1)
# print(arr)
# worker2 = honey(N,M,C)
# print(worker2)
# print(arr)
T = int(input())
for tc in range(T):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    worker1 = honey(N,M,C)
    worker2 = honey(N,M,C)
    print(f"#{tc+1} {worker1 + worker2}")