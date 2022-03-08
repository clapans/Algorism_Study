# 😇1859

## 👺필요한 개념

- 순회

- 최댓값찾기

## 👺풀이과정

- 마지막 가격을 최대값으로 설정한 후, 순회를 통해 최댓값 찾기
- 찾은 최댓값에 순회하는 가격을 빼서 저장

## 👺코드

```python
#케이스입력
num = int(input())

#케이스만큼 실행
for tc in range(1,num+1):
    N = int(input())
    
    #가격입력
    board = list(map(int, input().split()))
    _max = board[-1]
    cnt=0
    #가격순회, 최댓값 찾기
    for i in range(N-2,-1,-1):
        if _max < board[i]:
            _max = board[i]
        else:
            cnt+= _max - board[i]

    print(f'#{tc} {cnt}')
        
        '''
        #1 4053
		#2 6385
        #3 26725
        #4 211514
        #5 4848198
        #6 49761546
        #7 500155606
        #8 4995241394
        #9 4999367498
        #10 4995633799

        
        
        '''


```

