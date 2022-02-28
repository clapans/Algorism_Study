# 😇SWEA1946

## 👺필요한 개념

- 스택?

- 슬라이싱

## 👺풀이과정

- 리스트에 일렬로 더해서 저장한 후, 그 리스트를 10씩 인덱싱 출력

## 👺코드

```python
#케이스 입력
num = int(input())

#케이스 실행
for tc in range(1,num+1):
    
    #알파벳 수
    case = int(input())

   
    lst1= []
    
    #알파벳 수 만큼 반복
    for _ in range(case):
        
        #알파벳과 숫자입력
        Alpha, num = input().split(" ")
        n= int(num)
        
        #리스트에 일렬로 저장
        
        lst1 = lst1 + list(Alpha*n)
        
		#출력
    print(f'#{tc}')
    for k in range(len(lst1)//10+1):
        for a in lst1[10 * k:10 * (k + 1)]:
            print(a, end="")
        print()
        
        '''
        #1
        AAAAAAAAAA
        BBBBBBBCCC
        CC
        
        
        '''


```

