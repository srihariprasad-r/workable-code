"""
Find the length of longest increasing subsequence of given array

nums = {10, 20, 30, 15, 15}; 

Output: 3
"""

def longestincreasingarray(array):    
    lis = [1 for i in range(len(array))]
    maxLength = 0
    for i in range(len(array)):
        for j in range(0, i):
            if array[i] > array[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    for x in range(len(lis)):
        if maxLength < lis[x]:
            maxLength = lis[x]

    return maxLength

array = [10, 20, 30, 15, 15]
output = longestincreasingarray(array)
print(output)