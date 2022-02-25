T = int(input())

for t in range(T):
    N = int(input())
    res=""
    for _ in range(N) :
        ci,ki = input().split()
        res+=ci*int(ki)

    print(f"#{t+1}")
    for i in range(0,len(res),10) :
        print(res[i:i+10])