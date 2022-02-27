for case in range(int(input())):
    print(f'#{case+1}',end=' ')
    strs = []
    for _ in range(5):
        strs.append(input().rstrip())
    cnt = 0
    while True:
        tmp = ''
        for t in strs:
            if cnt < len(t):
                tmp += t[cnt]
        if not tmp:
            break
        print(tmp,end='')
        cnt += 1
    print('')