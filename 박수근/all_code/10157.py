import sys

c,r = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline())

cover = [1,1]
start = 1

while c > 0 or r > 0:
    end = start + 2 * (c + r) - 4
    if start <= n < end:
        if max(start + r - 1,n) == start + r - 1:
            print(cover[0],n - start + cover[1])
            quit(0)
        else:
            start += r - 1
        if max(start + c - 1,n) == start + c - 1:
            print(n - start + cover[0], cover[1] + r - 1)
            quit(0)
        else:
            start += c - 1
        if max(start + r - 1,n) == start + r - 1:
            print(cover[0] + c - 1,cover[1] + r - 1 - (n - start))
            quit(0)
        else:
            start += r - 1
        if max(start + c - 1,n) == start + c - 1:
            print(cover[0] + c - 1 - (n - start), cover[1])
            quit(0)
        else:
            start += c - 1
    else:
        start = end
        c -= 2
        r -= 2
        cover[0] += 1
        cover[1] += 1

print(0)