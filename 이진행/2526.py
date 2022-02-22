import sys
li = list(map(int, sys.stdin.readline().split(" ")))

ui=[]
ux=[]
a= li[2]-li[0]
b= li[3]-li[1]
c= li[6]-li[4]
d= li[7]-li[5]

ui.append(a)
ui.append(b)
ux.append(c)
ux.append(d)


print(ui,ux)
# if li[0] or li[2] == li[4] or li[6]:
#     print('b')