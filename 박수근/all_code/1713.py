import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

r = list(map(int,sys.stdin.readline().split()))

arr = {}
sumCnt = 0
for t in range(len(r)):
  try:
    arr[r[t]][0] += 1
  except:
    if len(arr) < n:
      arr[r[t]] = [1,t]
    else:
      min_ = int(1e9)
      tmp = []
      for k,v in arr.items():
        if v[0] < min_:
          min_ = v[0]
          tmp = [k]
        elif v[0] == min_:
          tmp.append(k)
      
      if len(tmp) > 1:
        minTime = int(1e9)
        minTmp = int(1e9)
        for k in tmp:
          if arr[k][1] < minTime:
            minTime = arr[k][1]
            minTmp = k
        del arr[minTmp]
      else:
        del arr[tmp[0]]
      arr[r[t]] = [1,t]

res = []

for k,v in arr.items():
  res.append(k)

print(*sorted(res))