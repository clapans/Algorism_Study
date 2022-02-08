import sys

s = sys.stdin.readline().rstrip()
word = list(sys.stdin.readline().rstrip())
stack = []
len_w = len(word)

for i in s:
    stack.append(i)
    if len(stack) >= len_w:
        if stack[-len(word):] == word:
            for i in range(len_w):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')

