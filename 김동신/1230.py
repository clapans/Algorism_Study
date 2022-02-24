# I 실행 함수
def I(code,x,y,s) :
    for j in s[::-1] :
        code.insert(x,j)
    return code

# D 실행 함수
def D(code,x,y) :
    for i in range(y) :
        del code[x]
    return code

# A 실행 함수
def A(code,y,s) :
    for j in s :
        code.append(j)
    return code


import sys
sys.stdin = open("input.txt")


for t in range(10):
    # 원본 코드의 길이
    N = int(input())
    # 원본 암호문
    code = input().split()
    # 명령어 개수
    M = int(input())
    # 명령어
    command = input().split()

    # pop으로 하나씩 제거해나가면서 함수 실행
    for _ in range(M) :
        if command[0] == "I" :  #command.pop(0) == "I"
            command.pop(0)
            xi = int(command.pop(0))
            yi = int(command.pop(0))
            si = [command.pop(0) for _ in range(yi)]
            code = I(code,xi,yi,si)

        elif command[0] == "D":
            command.pop(0)
            xd = int(command.pop(0))
            yd = int(command.pop(0))
            code = D(code, xd, yd)

        elif command[0] == "A":
            command.pop(0)
            ya = int(command.pop(0))
            sa = [command.pop(0) for _ in range(ya)]
            code = A(code, ya, sa)

    # 10개 항만 출력
    result = code[:10]

    print(f'#{t+1}')
    print(*result)