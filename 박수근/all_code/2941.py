
import sys

s = sys.stdin.readline().rstrip()
res = ''
cnt = 0

while cnt < len(s):
    try:
        if s[cnt:cnt+3] == 'dz=':
            res += '0'
            cnt += 3
            continue
        if s[cnt:cnt+2] in ['lj','nj','c=','c-','d-','s=','z=']:
            res += '0'
            cnt += 2
            continue
    except:
        pass
    res += s[cnt]
    cnt += 1

print(len(res))

import sys

s = sys.stdin.readline().rstrip()
for i in ['dz=','lj','nj','c=','c-','d-','s=','z=']:
    s = s.replace(i,'0')

print(len(s))
