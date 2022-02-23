for case in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    res = 0
    while nums:
        ix = nums.index(max(nums))
        res += nums[ix] * ix - sum(nums[:ix])
        nums = nums[ix+1:]
    print(f'#{case+1} {res}')