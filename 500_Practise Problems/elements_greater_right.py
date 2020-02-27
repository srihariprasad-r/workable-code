"""
Input = {10,4,6,5,3}

Output = {10,6,5,3}
"""

def rightelementgreater(array):
    poplist = []
    for i in range(len(array)):
        if len(poplist) != 0 and poplist[-1] < array[i]:            
            #print(poplist[-1])
            poplist.pop()     
        poplist.append(array[i])
    return poplist


array = [10,4,6,5,3]
array_output = rightelementgreater(array)
print(array_output)