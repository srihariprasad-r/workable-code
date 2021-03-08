from collections import deque

q = deque()

def balancedbracket(str):
    for i in range(len(str)):
        if str[i] == '[' or str[i] == '(' or str[i] == '{':
            q.append(str[i])
        else:
            if str[i] == ')':
                if len(q) > 0 and q[-1] == '(':
                    q.pop()
            elif str[i] == ']':
                if len(q) > 0 and q[-1] == '[':
                    q.pop()
            elif str[i] == '}':
                if len(q) > 0 and q[-1] == '{':
                        q.pop()
    if len(q) == 0:
        return True
    else:
        return False

str= "[(a+b){+c+d}]"
print(balancedbracket(str))