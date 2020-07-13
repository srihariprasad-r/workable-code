"""
A number spiral is an infinite grid whose upper-left square has number 1. Here are the first five layers of the spiral

Your task is to find out the number in row y and column x.

Input:
3
2 3
1 1
4 2

Output:
8
1
15
"""

def numberSpiral(y,x):
    maxNum = max(y, x)
    output = 0
    if (maxNum % 2 == 0):
        if x == maxNum:
            output = (maxNum-1)**2 + y
        else:
            output = (maxNum-1)**2 + (maxNum * 2) - x
    else:
        if y == maxNum:
            output = (maxNum-1)**2 + x
        else:
            output = (maxNum-1)**2 + (maxNum * 2) - y 
    
    print(output)

numberSpiral(1, 5)