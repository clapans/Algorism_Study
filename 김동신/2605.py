N=int(input()) #5
numbers=list(map(int,input().split())) #0 1 1 3 2

# 학생들 번호 나열
students = [x for x in range(1,N+1)] #1 2 3 4 5

# 학생들은 뽑은 번호 수만큼 앞에 사람과 자리를 바꾼다
for idx, number in enumerate(numbers) :
    for _ in range(number) :
        students[idx], students[idx-1] = students[idx-1], students[idx]
        idx -= 1  # 본인의 자리가 바뀌었으므로 idx에서도 1을 빼준다

for student in students :
    print(student, end=" ")