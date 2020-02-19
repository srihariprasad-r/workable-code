"""
Input = [1,1,0,1,1,1,0,0,1,1,1,1]
Output  = 4
"""

def maximumones(array):
    count_1 = 0
    prev_count = 0 
    for i in array:
        if i == 1:
            count_1 += 1
        else:
            prev_count = count_1
            count_1 = 0

    return max(prev_count, count_1)

array = [1,1,0,1,1,1,0,0,1,1,1,1]
output = maximumones(array)
print(output)