import sys
sys.stdin = open('input.txt')

num = int(input())

for tc in range(1,num+1):
    case = int(input())

    lst = []
    lst1= []
    for _ in range(case):
        Alpha, num = input().split(" ")
        n= int(num)
        lst.append(Alpha*n)
        lst1 = lst1 + list(Alpha*n)

    print(f'#{tc}')
    for k in range(len(lst1)//10+1):
        for a in lst1[10 * k:10 * (k + 1)]:
            print(a, end="")
        print()