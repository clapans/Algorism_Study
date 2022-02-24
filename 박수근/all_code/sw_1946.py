for case in range(int(input())):
    n = int(input())
    print(f'#{case+1}',end='')
    cnt = 0
    for t in range(n):
        tmp = input().split()
        for _ in range(int(tmp[1])):
            if not cnt % 10:
                print('')
            print(tmp[0],end='')
            cnt += 1
    print('')