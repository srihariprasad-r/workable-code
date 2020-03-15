"""
this function will arrange them in such way that the arrangement will form the largest value.
Input = {3, 1, 13, 34, 8}

Output = 8343131
"""

def arrangeNumber(array):
    n = len(array)
    for i in range(n):
        for j in range(n):
            if str(array[i]) + str(array[j]) > str(array[j]) + str(array[i]):
                if i > j:
                    array[i], array[j] = array[j], array[i]
    
    return ''.join(map(str,array)) #map function expects 2 arguments, function to be applied and sequence on which it should run


array = [3, 1, 13, 34, 8]
array_o = arrangeNumber(array)
print(array_o)