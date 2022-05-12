import sys

n = int(sys.stdin.readline())
data = {}
cal = []
for i in range(n):
    tmp = sys.stdin.readline()
    for j in range(len(tmp)):
        try:
            data[tmp[j]] += 10**(len(tmp)-j-1)
        except:
            data[tmp[j]] = 10**(len(tmp)-j-1)
    cal.append(tmp)
    
data = sorted(data.items(),key = lambda x: x[1],reverse=True)

m = 9
ix = {}
s = 0

for i in data:
    ix[i[0]] = m
    m -= 1
    
for i in cal:
    tmp = ""
    for j in i:
        tmp += str(ix[j])
    s += int(tmp)

print(s)