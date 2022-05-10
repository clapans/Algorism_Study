import sys

l,c = map(int,sys.stdin.readline().split())
letters = sys.stdin.readline().split()

letters.sort()
case = ["a","e","i","o","u"]

def dfs(x,password):
    if x == c:
        if len(password) == l:
            a_cnt,b_cnt = 0,0
            for i in password:
                if i in case:
                    a_cnt += 1
                else:
                    b_cnt += 1
            if a_cnt > 0 and b_cnt > 1:
                print(''.join(password))
    else:
        password.append(letters[x])
        dfs(x+1,password)
        password.pop()
        dfs(x+1,password)

dfs(0,[])