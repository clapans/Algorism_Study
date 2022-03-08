# 😇SWEA5356

## 👺필요한 개념

- 곱하는 방법, 2중 for문에 if문으로 조건에 해당하는 값만 구하기

## 👺풀이과정

- 단조 체크함수를 정의한다. 밑에 테스트 케이스 실행하는 구문에서 int를 str로 변한한 후 다시 int로 변환하는 경우, 시간초과가 발생한다. 따라서 함수를  Ture, False만 반환하도록 정의한다.

## 👺코드

```python

#단조 체크함수 정의
def check(num):
    a= str(num)
    for k in range(len(a)-1):
        if a[k] > a[k+1]:
            return False
    return True

#테스트 케이스입력
T = int(input())

for tc in range(1,T+1):
    #입력 숫자
    n = int(input())

    #입력 리스트
    lst1 = list(map(int, input().split()))

    #곱셈 리스트
    #[2, 4, 7, 10]
    #lst[0]*lst[1], lst[0]*lst[2] 이런식으로 곱해감 그중 10보다 큰값만 저장
    lst2=[]
    for a in range(n):
        for j in range(n):
            if a<j:
                if lst1[a]*lst1[j]>10:
                    lst2.append(lst1[a]*lst1[j])
    
    
    tmp=0
    for a in lst2:
        #단조증가일 경우 가장 큰값 tmp에 저장
        if check(a):
            tmp = max(tmp,a)


	#tmp가 0인 경우, -1 출력하도록
    if tmp==0:
        tmp=-1

    print(f'#{tc} {tmp}')
```

