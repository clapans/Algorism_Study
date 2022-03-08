# 😇SWEA5356 세로로 말해요

## 👺필요한 개념

- 인덱싱

## 👺풀이과정

- 입력받은 리스트 중 문자열의 길이가 가장 긴 값을 구한다.
- 순회를 하면서 문자열의 길이가 가장 긴 문자열의 보다 작은 경우 추가하지 않는다.

## 👺코드

```python
#케이스입력
T = int(input())

for tc in range(1,T+1):
    #입력 리스트
    lst1 = []
    for i in range(5):
        lst1.append(input())

    

    #가로로 가장 긴값 찾기
    max_len = 0
    for r in lst1:
        if len(r)>max_len:
            max_len = len(r)
            
    #가장 긴값 보다 해당 입력 길이가 작으면 추가X
    stp = ''
    for i in range(max_len):
        for j in range(5):
            if i < len(lst1[j]):
                stp+=lst1[j][i]
                
    #출력
    print(f'#{tc} {stp}')
```

