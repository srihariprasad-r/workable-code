"""
Given array of integers, You want to modify the array so that it is increasing, 
i.e., every element is at least as large as the previous element.

array = [3, 2, 5, 1, 7]

Output = 5
"""

def increasingArray(n, array):
    maxValue = 0
    ans = 0
    for i in range(len(array)):
        maxValue = max(maxValue, array[i])
        ans += maxValue - array[i]
    
    return ans

array =  [3, 2, 5, 1, 7]
increasingArray(5, array)