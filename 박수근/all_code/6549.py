import sys

def tree(s,e,ix):
    if s == e:
        seg[ix] = height[s]
        return seg[ix]
    mid = (s+e)//2
    seg[ix] = min(tree(s,mid,ix*2),tree(mid+1,e,ix*2+1))
    return seg[ix]

def get(s,e,l,r,ix):
    if r < s or l > e:
        return int(1e9)
    if l <= s and r >= e:
        return seg[ix]
    mid = (s+e)//2
    return min(get(s,mid,l,r,ix*2),get(mid+1,e,l,r,ix*2+1))

while True:
    height = list(map(int,sys.stdin.readline().split()))
    if not height[0]:
        break
    seg = [[] for _ in range((4*pow(int(height[0]**(1/2))+1,2)))]
    res = 0
    tree(1,height[0],1)
    for i in range(1,height[0]+1):
        if res > height[i] * (height[0]-i+1):
            continue
        for j in range(i,height[0]+1):
            tmp = get(1,height[0],i,j,1)
            if res > (height[0]-i+1) * tmp:
                break 
            res = max(res,tmp * (j-i+1))
    print(res)