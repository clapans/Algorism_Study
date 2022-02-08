import sys

n = int(sys.stdin.readline())
dice = []
res_ = 0
dic_ = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
for i in range(n):
    dice.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,7):
    cnt = 0
    down = i
    res = 0
    while cnt < n:
        up = dice[cnt][dic_[dice[cnt].index(down)]]     # 윗면 숫자
        res += max([_ for _ in [1,2,3,4,5,6] if _ not in [down,up]])
        down = up
        cnt += 1
    res_ = max(res_,res)

print(res_)