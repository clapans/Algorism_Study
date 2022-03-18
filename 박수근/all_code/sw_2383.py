import heapq

def lunch(x,time):
    global res
    if x == len(person):
        tmp = 0
        for i in range(len(time)):
            k = arr[stair[i][0]][stair[i][1]]

            for j in range(len(time[i])):
                while len(time[i][j]) > 3:
                    pop_ = heapq.heappop(time[i][j])
                    try:
                        heapq.heappush(time[i][j+int(k)],pop_)
                    except:
                        time[i].append([pop_])
            tmp = max(tmp,len(time[i]))
        res = min(res,tmp)
    else:
        time_save = [[v[:] for v in t] for t in time]
        for t in range(len(stair)):
            k = arr[stair[t][0]][stair[t][1]]
            r = abs(person[x][0] - stair[t][0])
            c = abs(person[x][1] - stair[t][1])
            while len(time[t]) < r+c+int(k)+1:
                time[t].append([])
            for i in range(r+c+1,r+c+int(k)+1):
                heapq.heappush(time[t][i],(-(r+c)))
            lunch(x+1,time)
            time = [[v[:] for v in t] for t in time_save]

for case in range(int(input())):
    n = int(input())
    arr = []
    person = []
    stair = []
    for _ in range(n):
        arr.append(input().split())
    res = int(1e9)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '1':
                person.append([i,j])
            elif arr[i][j] == '0':
                pass
            else:
                stair.append([i,j])
    lunch(0,[[] for t in stair])
    print(f'#{case+1} {res}')