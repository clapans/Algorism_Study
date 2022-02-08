n = int(input())
li = [t for t in range(1,n)] + [n-1]
numbers = []
res = 0

for i in range(n):
    numbers.append(int(input()))

for x,y in zip(sorted(numbers,reverse=True),li):
    res += x*y

print(res)    


