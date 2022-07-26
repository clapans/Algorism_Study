import sys
import heapq

t = int(sys.stdin.readline())
        
for case in range(t):
    k = int(sys.stdin.readline())
    max_ = []
    min_ = []
    min_save, max_save = [],[]

    for _ in range(k):
        a,b = sys.stdin.readline().split()
        if a == "I":
            b = int(b)
            heapq.heappush(max_,-b)
            heapq.heappush(min_,b)
        else:
            if b == "1":
                try:
                    while True:
                        tmp = heapq.heappop(max_)
                        if len(min_save) == 0 or tmp != min_save[0]:
                            heapq.heappush(max_save,-tmp)
                            break
                        else:
                            heapq.heappop(min_save)
                except:
                    pass
            else:
                try:
                    while True:
                        tmp = heapq.heappop(min_)
                        if len(max_save) == 0 or tmp != max_save[0]:
                            heapq.heappush(min_save,-tmp)
                            break
                        else:
                            heapq.heappop(max_save)
                except:
                    pass 
    
    try:
        while True:
            tmp = heapq.heappop(max_)
            if len(min_save) == 0 or tmp != min_save[0]:
                print(-tmp,end=" ")
                break
            else:
                heapq.heappop(min_save)
    except:
        print("EMPTY")
        continue

    try:
        while True:
            tmp = heapq.heappop(min_)
            if len(max_save) == 0 or tmp != max_save[0]:
                print(tmp)
                break
            else:
                heapq.heappop(max_save)
    except:
        print("EMPTY")