N = int(input())
farm = [list(map(int, input().split())) for _ in range(6)]
farm2 = list(map(list,zip(*farm)))
big_area = 1
small_area = 1
not_small = []

for i in range(6):
    if farm2[0].count(farm2[0][i]) == 1:
        big_area *= farm2[1][i]
        if i == 5:
            not_small.append(0)
            not_small.append(i-1)
        elif i == 0:
            not_small.append(i+1)
            not_small.append(5)
        else:
            not_small.append(i+1)
            not_small.append(i-1)


for j in range(6):
    if j not in not_small:
        small_area *= farm2[1][j]    

print(N*(big_area-small_area))

