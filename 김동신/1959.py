T = int(input())

for t in range(T) :

    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    total_max = 0
    if N<M :
        i = 0
        while i<=M-N :
            total = 0
            for k in range(N) :
                total += A[k]*B[i+k]
            i+=1
            if total>total_max :
                total_max = total
    else :
        i = 0
        while i<=N-M :
            total = 0
            for k in range(M) :
                total += B[k]*A[i+k]
            i+=1
            if total>total_max :
                total_max = total
    print(f"#{t+1} {total_max}")