s = input().rstrip()
re_s = ""
state = 0
tmp = ""

for i in s:
    if i == "<":
        re_s += ''.join([t for t in tmp[::-1]]) + i
        tmp = ""
        state = 1
    elif i == ">":
        re_s += i
        state = 0
    else:
        if state == 1:
            re_s += i
        else:
            if i == " ":
                re_s += ''.join([t for t in tmp[::-1]]) + i
                tmp = ""
            else:
                tmp += i
print(re_s + ''.join([t for t in tmp[::-1]]))