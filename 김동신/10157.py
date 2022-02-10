garo,saero = map(int,input().split(" "))
K=int(input())

if K>garo*saero :
    print(0)

else :
    seat = []
    tmp=[]
    for y in range(saero,0,-1) :
        for x in range(1,garo+1) :
            tmp.append((x, y))
        seat.append(tmp)
        tmp=[]

# ----------------------------------------------------------- #

    temp = []
    m = 1
    n = 0
    while True:
        # 왼쪽 세로
        for i in range(saero - m, m - 2, -1):
            temp.append(seat[i][n])

        if len(temp) >= garo * saero:
            break

        # 위에 가로
        for j in range(n + 1, garo - m):
            temp.append(seat[n][j])

        if len(temp) >= garo * saero:
            break

        # 오른쪽 세로
        for k in range(m - 1, saero - (m - 1)):
            temp.append(seat[k][garo - m])

        if len(temp) >= garo * saero:
            break

            # 아래 가로
        for l in range(garo - m - 1, m - 1, -1):
            temp.append(seat[saero - m][l])
        if len(temp) >= garo * saero:
            break

        m += 1
        n += 1

    result = temp[K - 1]
    for res in result:
        print(res, end=" ")