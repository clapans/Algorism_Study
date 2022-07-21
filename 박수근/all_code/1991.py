import sys

def PreOrder(root):
    print(root, end= "")
    for element in dic[root]:
        if element != '.':
            PreOrder(element)
    
def InOrder(root):
    if dic[root][0] != '.':
        InOrder(dic[root][0])
    print(root, end = "")
    if dic[root][1] != '.':
        InOrder(dic[root][1])
    
def PostOrder(root):
    for element in dic[root]:
        if element != '.':
            PostOrder(element)
    print(root, end = "")
    
n = int(sys.stdin.readline())
dic = {}

for _ in range(n):
    root,left,right = sys.stdin.readline().split()
    dic[root] = [left,right]

PreOrder("A")
print("")
InOrder("A")
print("")
PostOrder("A")