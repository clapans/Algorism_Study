## 1. 딕셔너리 원소 추가



```python
a = {'h' : 1, 'e' : 2, 'l' : 3}
a['o'] = 4
print(a)

#= {'h' : 1, 'e' : 2, 'l' : 3, 'o' : 4}
```



## 2. 딕셔너리 value 값 변경



### 정수 value의 연산

```python
a = {'h' : 1, 'e' : 2, 'l' : 3}
a['h'] += 1; a['e'] -= 1; a['l'] = a['l']//2
print(a)

#= {'h' : 2, 'e' : 1, 'l' : 1}
```



### 문자열 value의 연산

```python
a = {'h' : '1', 'e' : '2', 'l' : '3'}
a['h'] += '0'
print(a)

#= {'h' : '11', 'e' : '2', 'l' : '3'}
```



## 3. 리스트 [-1] 원소 삭제

```python
a = [1,2,3,4,5,6]
tmp = a.pop()
print(tmp,a)

#= 6, [1,2,3,4,5]
```



## 4. count

```python
a = [1,1,1,1,2,2]
print(a.count(1))

#= 4
```

문자열에서도 가능, 튜플에서 불가능



## 5. index

```python
a = [1,2,3,4,5]
print(a.index(5))

#= 4
```

lst.index(value) 

value 값을 갖는 리스트 index를 반환



