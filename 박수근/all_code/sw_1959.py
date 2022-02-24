def iterate(x,y):
    global res
    for i in range(len(x)-len(y)+1):
        tmp = 0
        for j in range(len(y)):
            tmp += x[i+j]*y[j]
        res = max(res,tmp)

for case in range(int(input())):
    n,m = map(int,input().split())
    nums1 = list(map(int,input().split()))
    nums2 = list(map(int,input().split()))
    res = 0
    if len(nums1) > len(nums2):
        iterate(nums1,nums2)
    else:
        iterate(nums2,nums1)
    print(f'#{case+1} {res}')