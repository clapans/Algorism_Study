import sys

arr = []

for _ in range(19):
  arr.append(list(map(int,sys.stdin.readline().split())))

def garo(x,y,color):
  if y > 14:
    return False
  if arr[x][y:y+5] == [color]*5:
    try:
      if arr[x][y+5] != color:
        return True
    except:
      return True
  return False

def sero(x,y,color):
  if x > 14:
    return False
  if arr[x][y] == color and arr[x+1][y] == color and arr[x+2][y] == color and arr[x+3][y] == color and arr[x+4][y] == color:
    try:
      if arr[x+5][y] != color:
        return True
    except:
      return True
  return False

def daegak(x,y,color):
  if y > 14:
    return False
  if x <= 14 and arr[x][y] == color and arr[x+1][y+1] == color and arr[x+2][y+2] == color and arr[x+3][y+3] == color and arr[x+4][y+4] == color and arr[x+5][y+5] != color:
    try:
      if arr[x+5][y+5] != color:
        return True
    except:
      return True
  if x >= 4 and arr[x][y] == color and arr[x-1][y+1] == color and arr[x-2][y+2] == color and arr[x-3][y+3] == color and arr[x-4][y+4] == color:
    if x == 4:
        return True
    try:
      if arr[x-5][y+5] != color:
        return True
    except:
      return True
  return False

for i in range(19):
  for j in range(19):
    if arr[i][j] != 0 and (garo(i,j,arr[i][j]) or sero(i,j,arr[i][j]) or daegak(i,j,arr[i][j])):
      print(arr[i][j])
      print(i+1,j+1)
      quit()
      
print(0)