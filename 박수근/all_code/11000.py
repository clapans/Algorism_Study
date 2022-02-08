import sys

n = int(input())
table = []

for i in range(n):
    table.append(list(map(int,input().split())))

table.sort(key = lambda x: (x[1],x[0]))
end_time = table[0][1]
cnt = 1

for i in table[1:]:
    if i[0] < end_time:
        pass
    else:
        end_time = i[1]
        cnt += 1

print(cnt)