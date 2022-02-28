# 😇SWEA1959

## 👺필요한 개념

- 순회

- 슬라이싱

## 👺풀이과정

- 덧셈작업 생각해 내는게 가장 어려웠다.
- 인덱싱으로 할지, 새로운 리스트를 만들어서 1:1대응 시킬지 고민했다.
- tmp로 max값을 구하고 다시 tmp를 초기화시켜주기

## 👺코드

```python
#케이스입력
num = int(input())

for tc in range(1,num+1):
    # N = len(Aj) M = len(Bj)
    N,M = map(int,input().split())
    
    #숫자리스트
    Aj = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    
    #Aj가 항상 길이가 작은값으로 만들어주기 
    if len(Aj) > len(Bj):
        Bj, Aj = Aj, Bj
        N, M = M, N
 
    #초기값
    cnt=0
    _max=0
    
    #덧셉작업
    for i in range(M-N+1):
        tmp = 0

        for j in range(N):
            tmp+=Aj[j]*Bj[j+i]
        
        #최대값 찾기
        if tmp>_max:
            _max=tmp
    #출력
    print(f'#{tc} {_max}')
```

