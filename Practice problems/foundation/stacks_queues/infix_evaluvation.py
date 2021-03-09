"""
Infix expression -> a + b where '+' refers to operator
Postfix expression -> ab+ 

we will consider 2 stacks, one for operand and other for operator
1. If we encounter digits/alphabets, we will push to operands
2. If operators, we will push to operator stack
3. When we encounter '(', we will add to operator
4. When we encounter, ')' we pop operator and we pop two elements from operands
    last element from operands which was first popped is v2
    last but one from operand is v1
5. we will continue this until we find '('
6. when we encounter operator, we check below:
  - when last element in operator stack has higher precedence, we pop that element, else we append
  - we stop pop of elements when we hit '('
7. There can be leftover in either of stacks in any of the cases, 
for ex: 2*3+6
In this case repeat same pop operation as above # 4
"""
def infixevaluvation(str):
    def predecense(op1):
        if op1 == '+' or op1 == '-':
            return 1
        elif op1 == '*' or op1 == '/':
            return 2
            
    
    def operation(v1, v2, op):
        if op == '+':
            return v1 + v2
        elif op == '-':
            return v1 - v2
        elif op == '*':
            return v1 * v2
        elif op == '/':
            return v1 // v2
            
    
    operator = []
    operand = []
    
    for i in range(len(str)):
        if str[i] == '(':
            operator.append(str[i])
        elif str[i].isdigit():
            operand.append(int(str[i]))
        elif str[i] == '+' or str[i] == '-' or str[i] == '*' or str[i] == '/':
            while len(operator) > 0 and operator[-1] != '(' and predecense(str[i]) <= predecense(operator[-1]):
                op = operator.pop()
                v2 = operand.pop()
                v1 = operand.pop()
                
                opv = operation(v1, v2, op)
                operand.append(opv)
            operator.append(str[i])
        elif str[i] == ')':
            while operator[-1] != '(':
                op = operator.pop()
                v2 = operand.pop()
                v1 = operand.pop()
                
                opv = operation(v1, v2, op)
                operand.append(opv)
            operator.pop()

    while len(operator) > 0:
        op = operator.pop()
        v2 = operand.pop()
        v1 = operand.pop()
                
        opv = operation(v1, v2, op)
        operand.append(opv)   
        
    return operand[-1]

str="((2*(6-1))/2)*4"
print(infixevaluvation(str))