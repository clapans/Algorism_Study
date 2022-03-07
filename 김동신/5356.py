T = int(input())

for tc in range(T):
    #단어의 최대길이는 15이고 단어의 최대 갯수는 5개
    #""으로 이루어진 배열을 만든다
    arr = [[""]*15 for _ in range(5)]

    #단어가 5개이므로 5번 나눠서 input
    for n in range(5) :
        words = input()
        for m in range(len(words)): #input받은 단어를 한글자씩 배열에 삽입
            arr[n][m] = words[m]

    print(f"#{tc+1}",end=" ")
    #세로로 한글자씩 읽고, 끝을 빈칸으로 출력
    for i in range(15) :
        for j in range(5) :
            print(arr[j][i],end="")
    print()