import heapq

for case in range(int(input())):
    n,m,k,lost_recept,lost_repair = map(int,input().split())
    recept = list(map(int,input().split()))
    repair = list(map(int,input().split()))
    res = [[-1]*m for _ in range(n)]
    recept_heap,repair_heap = [],[]
    for i in range(n):
        heapq.heappush(recept_heap,i)
    for i in range(m):
        heapq.heappush(repair_heap,i)
    recept_time = [recept_heap[:] for _ in range(2500)]
    repair_time = [repair_heap[:] for _ in range(2500)]
    customer = []
    for ix,v in enumerate(list(map(int,input().split()))):
        heapq.heappush(customer,(v,ix))
    waiting = []
    waiting_repair = []
    cur_time = customer[0][0]
    while customer or waiting or waiting_repair:
        while customer and cur_time == customer[0][0]:
            tmp = heapq.heappop(customer)
            heapq.heappush(waiting,(tmp[1],tmp[0]))
        while recept_time[cur_time] and waiting:
            r_tmp = heapq.heappop(waiting)
            tmp = heapq.heappop(recept_time[cur_time])
            heapq.heappush(waiting_repair,(cur_time+recept[tmp],tmp,r_tmp[0]))
            for i in range(cur_time+1,cur_time+recept[tmp]):
                recept_time[i].remove(tmp)
        while repair_time[cur_time] and waiting_repair:
            if cur_time >= waiting_repair[0][0]:
                r_tmp = heapq.heappop(waiting_repair)
                tmp = heapq.heappop(repair_time[cur_time])
                for i in range(cur_time+1,cur_time+repair[tmp]):
                    repair_time[i].remove(tmp)
                if res[r_tmp[1]][tmp] == -1:
                    res[r_tmp[1]][tmp] = r_tmp[2] + 1
                else:
                    res[r_tmp[1]][tmp] += r_tmp[2] + 1
            else:
                break
        cur_time += 1
    print(f'#{case+1} {res[lost_recept-1][lost_repair-1]}')