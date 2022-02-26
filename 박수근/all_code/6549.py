import sys

def tree(s,e,ix):
    if s == e:
        seg[ix] = [height[s],s]
        return seg[ix]
    mid = (s+e)//2
    tmp1,tmp2 = tree(s,mid,ix*2),tree(mid+1,e,ix*2+1)
    seg[ix] = tmp1 if tmp1[0] < tmp2[0] else tmp2
    return seg[ix]

def get(s,e,l,r,ix):
    if r < s or l > e:
        return int(1e9)
    if l <= s and r >= e:
        return seg[ix]
    mid = (s+e)//2
    tmp1,tmp2 = get(s,mid,l,r,ix*2),get(mid+1,e,l,r,ix*2+1)
    return tmp1 if tmp1[0] < tmp2[0] else tmp2

def sep_(s,e):
    val,ix = get(1,height[0],s,e,1)
    return max(sep_(s,ix-1),sep_(ix+1,e),val*(e-s+1)) 

while True:
    height = list(map(int,sys.stdin.readline().split()))
    if not height[0]:
        break
    seg = [[] for _ in range((4*pow(int(height[0]**(1/2))+1,2)))]
    res = 0
    tree(1,height[0],1)