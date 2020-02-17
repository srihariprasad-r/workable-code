"""
Input = {1,0,1,0,1,0,0,1}

Output = {0,0,0,0,1,1,1,1}
"""

def binary_array_sort(array):
    newarray = []
    k = 0
    alen = len(array)
    count0 = array.count(0)
    while(count0 != 0):
        newarray.append(0)
        count0 -= 1
        k += 1
    
    while(k < alen):
        newarray.append(1)
        k +=1 
    
    return newarray


array = [1,0,1,0,1,0,0,1]
output = binary_array_sort(array)
print(output)
