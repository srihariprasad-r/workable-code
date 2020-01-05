def isValid(s):
    if (len(s) %2 != 0):
        return 'false'
    
    stack_list = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack_list.append(i)
        elif (i == ')' and len(stack_list) > 0 and stack_list[-1] == '('):
            stack_list.pop()
        elif (i == '}' and len(stack_list) > 0 and stack_list[-1] == '{'):
            stack_list.pop()            
        elif (i == ']' and len(stack_list) > 0 and stack_list[-1] == '['):
            stack_list.pop()             
    
    return not stack_list


input_str =  "["
a = isValid(input_str)
print(a)


    