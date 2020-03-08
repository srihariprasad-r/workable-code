"""
Input = {1, 2, 0, 4, 3, 0, 5, 0}
Output = {1, 2, 4, 3, 5, 0, 0}
"""

def shiftarray(array):
    count = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[count] = array[i]
            count += 1
    
    while (count< len(array)):
        array[count] = 0
        count += 1
    
    return array

array = [1, 2, 0, 4, 3, 0, 5, 0]
output = shiftarray(array)
print(output)