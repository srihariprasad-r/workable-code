"""
Find index which divies array into equal sum
Input : {-1,6,1,-2,3,3}

Output = 2 
"""

def arraydividesum(array):
    total = 0
    left_sum = array[0]
    for i in range(len(array)):
        total += array[i]
    
    for i in range(1, len(array)):
        if left_sum == total - (array[i] + left_sum):
            return i
        else:
            left_sum += array[i]

array  = [-1,6,1,-2,3,3]
output = arraydividesum(array)
print(output)

