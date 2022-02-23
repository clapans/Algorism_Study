# 😇2491

## 👺필요한 개념

- 리스트 순회

- 큰 값을 반환하는 if문 활용

## 👺풀이과정

- 올림 순열, 내림 순열을 각각 for문을 활용하여 검색
- 예를들어 리스트K[a]>=K[a-1]인 경우 카운트를 함
- 카운트 한 최대 횟수를 max_1 변수에 저장을 함
- 조건에 해당되지 않는 경우 카운트 변수를 1로 최기화함

## 👺코드

```python
for ca in range(1,4):
    N = int(input())
    K = list(map(int, input().split()))


    #비교할 값
    cnt = 1
    max_1 = 1

    #탐색, 수열 커지는 방향 탐색
    for a in range(1,N):
        if K[a]>=K[a-1]:
            cnt+=1
        else:
            cnt=1

        #가장 큰 값 도출
        if max_1 < cnt:
            max_1 = cnt


    #탐색, 수열 작아지는 방향 탐색
    for a in range(1,N):
        if K[a] <=K[a-1]:
            cnt+=1
        else:
            cnt=1

        #가장 큰 값 도출
        if max_1 < cnt:
            max_1 = cnt


    print(max_1)
    
    
8
4
2

```

