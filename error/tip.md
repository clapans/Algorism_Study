##  입력 받는 시간 줄이는 법



input() 함수 대신 sys.stdin.readline() 을 사용하면 입력받는 시간을 줄일 수 있습니다.

대신 VScode나 파이참으로 실행시킬 때 에러가 발생할 겁니다(잘은 모르는데 파일단위로 입력받는 거여서 그럴거에요.)



```python
import sys

n = sys.stdin.readline()	# n = '문자열' 형태로 저장
n = sys.stdin.readline().split()	# 공백으로 구분하고 한 줄로 입력받음 ex)>>5 7 6 8
									# n = '리스트' 형태로 저장, 각 원소들은 str 타입
a,b = sys.stdin.readline().split()	# 공백으로 구분하고 한 줄로 입력받음
									# a,b에 각각 입력받은 데이터가 str 타입으로 들어감
n = list(map(int,sys.stdin.readline().split()))	# 공백으로 구분하고 한 줄로 입력받음
									# n = '리스트' 형태로 저장, 각 원소들은 int 타입
n = sys.stdin.readline().strip()	# n = '문자열' 형태로 저장 n에 앞뒤로 공백 제거
```

