for case in range(10):
    n = int(input())
    pw = [0] + list(map(int,input().split()))
    cmd = int(input())
    cmds = list(input().split())
    cnt = 0
    while cnt < len(cmds):
        if cmds[cnt] == 'I':
            pw = pw[:int(cmds[cnt+1])+1] + cmds[cnt+3:cnt+3+int(cmds[cnt+2])] + pw[int(cmds[cnt+1])+1:]
            cnt += int(cmds[cnt+2]) + 3
        elif cmds[cnt] == 'D':
            pw = pw[:int(cmds[cnt+1])+1] + pw[int(cmds[cnt+1])+cnt+1:]
            cnt += 3
        elif cmds[cnt] == 'A':
            pw += cmds[cnt+2:cnt+2+int(cmds[cnt+1])]
            cnt += int(cmds[cnt+1]) + 2
        else:
            pass

    print('#',case+1,end=' ',sep='')
    print(*pw[1:11])