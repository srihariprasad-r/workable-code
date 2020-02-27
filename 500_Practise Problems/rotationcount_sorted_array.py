"""
Input = {15, 18, 2, 3, 6, 12}

Output: 2
Explanation : Initial array must be {2, 3,
6, 12, 15, 18}. We get the given array after 
rotating the initial array twice.
"""

def rotationcount(array):
    min, index = array[0] , 0
    for i in range(len(array)):
        if min > array[i]:
            min = array[i]
            index = i
    
    return index

array = [15, 18, 2, 3, 6, 12]
output = rotationcount(array)
print(output)
