def ch_sort(x):
    for t in range(1,len(x)):
        if x[t] < x[t-1]:
            return -1
    return int(x)

for case in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    multi = set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            multi.add(nums[i]*nums[j])
    multi = sorted(list(multi),reverse=True)
    for t in multi:
        tmp = ch_sort(str(t))
        if tmp != -1:
            break
    print(f'#{case+1} {tmp}')
