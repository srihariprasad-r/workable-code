def infixconversion(str):
    def predecense(op):
        if op == '+' or op == '-':
            return 1 
        elif op == '*' or op == '/':
            return 2
            
    
    operator = []
    prefix = []         #to hold prefix values
    postfix = []        # postfix values
    
    for i in range(len(str)):
        if str[i] == '(':
            operator.append(str[i])
        elif str[i] == ')':
            while len(operator) > 0 and operator[-1] != '(':
                op = operator.pop()
                v2 = prefix.pop()
                v1 = prefix.pop()
                
                prefix_opv = op + v1 + v2
                prefix.append(prefix_opv)
                v2 = postfix.pop()
                v1 = postfix.pop()
                
                postfix_opv = v1 + v2 + op
                postfix.append(postfix_opv)   
            operator.pop()
        elif str[i] == '+' or str[i] == '-' or str[i] == '*' or str[i] == '/':
            while len(operator) > 0 and operator[-1] != '(' and predecense(str[i]) <= predecense(operator[-1]):
                op = operator.pop()
                v2 = prefix.pop()
                v1 = prefix.pop()
                
                prefix_opv = op + v1 + v2
                prefix.append(prefix_opv)
                v2 = postfix.pop()
                v1 = postfix.pop()
                
                postfix_opv = v1 + v2 + op
                postfix.append(postfix_opv)      
            operator.append(str[i])
        else:
            prefix.append(str[i])
            postfix.append(str[i])
            
    while len(operator) > 0:
        op = operator.pop()
        if len(prefix) > 0:
            v2 = prefix.pop()
            v1 = prefix.pop()
                
        prefix_opv = op + v1 + v2
        prefix.append(prefix_opv)
        if len(postfix) > 0 :
            v2 = postfix.pop()
            v1 = postfix.pop()
                
        postfix_opv = v1 + v2 + op
        postfix.append(postfix_opv)
        
    return prefix[-1], postfix[-1]

str = "a*(b-c)/d+e"
print(infixconversion(str))