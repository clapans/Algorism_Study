from collections import deque

n,w,l = map(int,input().split())
trucks = list(map(int,input().split()))
queue = deque([0]*w)
sum = 0
time,passCnt = 0,0
num = 0

def delete():
    global sum
    global passCnt
    tmp = queue.popleft()
    if tmp != 0:
        sum -= tmp
        passCnt += 1
    queue.append(0)

def insert(weight):
    global sum
    global num
    if sum + weight <= l:
        queue.pop()
        sum += weight
        num += 1
        queue.append(weight)

while True:
    if passCnt == n:
        break
    delete()
    if num < n:
        insert(trucks[num])
    time += 1

print(time)