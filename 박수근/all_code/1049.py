import sys

n,m = map(int,sys.stdin.readline().split())
price = [-1,-1]

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    if price == [-1,-1]:
        price = [a,b]
    else:
        price = [min(price[0],a),min(price[1],b)]

if price[0] < 6* price[1]:
    print(price[0] * (n//6) + min(price[0],price[1] * (n % 6)))
else:
    print(price[1] * n)