import sys

n = int(sys.stdin.readline())
res = []

for i in range(n+1):
    numbers = [n,i]
    while True:
        if numbers[-2] - numbers[-1] < 0:
            break
        numbers.append(numbers[-2] - numbers[-1])
    if len(numbers) > len(res):
        res = numbers[:]

print(len(res))
print(*res)
