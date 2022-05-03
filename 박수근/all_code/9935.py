import sys

word = sys.stdin.readline().rstrip()
explode = list(sys.stdin.readline().rstrip())
stack = []

for i in word:
    stack.append(i)
    if len(stack) >= len(explode) and stack[-len(explode):] == explode:
        for j in range(len(explode)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')