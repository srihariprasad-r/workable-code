"""
Input = {1, 56, 58, 57, 90, 92, 94, 93, 91, 45}

Output = 5
"""

def longerSubArray(array,n):    
    array_len = 0
    for i in range(n-1):
        mx = mn = array[i]
        for j in range(i+1,n):
            mx = max(mx, array[j])
            mn = min(mn, array[j])        

            if ((mx - mn) == j-i):
                array_len = max(array_len, mx-mn+1)    
    return array_len

array = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
output = longerSubArray(array, len(array))
print(output)