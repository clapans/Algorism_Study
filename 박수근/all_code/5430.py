import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    lst = deque(sys.stdin.readline()[1:-2].split(","))
    
    direction = 1

    def func():
        global direction
        for t in p:
            if t == 'R':
                direction = -direction
            else:
                if direction == 1:
                    if lst:
                        lst.popleft()
                    else:
                        return "error"
                else:
                    if lst:
                        lst.pop()
                    else:
                        return "error"
        if not lst:
            return "error"
        string = '['
        if direction == 1:
            for t in lst:
                string += t + ','
        else:
            for t in list(lst)[::-1]:
                string += t + ','
                
        string = string[:-1] + ']'
        return string

    print(func())
            
    
    
    
                