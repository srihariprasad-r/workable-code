"""
Input = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
Output = 9
"""

def maximum_index_at_0(array):    
    sum_1 = 0
    prev_sum = 0
    for i in range(0,len(array)):
        if array[i] != 0 :
            sum_1 += 1
        else:
            prev_sum = sum_1
            sum_1 = 0 
        
        

array = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
maximum_index_at_0(array)