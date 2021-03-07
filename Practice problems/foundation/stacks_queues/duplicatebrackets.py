from collections import deque

q = deque()

def duplicatebracket(str):

    for i in range(len(str)):
        if str[i] != ')':
            q.append(str[i])
        else:
            if q[-1] == '(':
                return True
            else:
                while q[-1] != '(':
                    q.pop()
                q.pop()

    return False

str = "(a+b)+((c+d))"
print(duplicatebracket(str))