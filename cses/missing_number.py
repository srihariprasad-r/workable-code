"""
You are given all numbers between 1,2,…,n except one. Your task is to find the missing number.

Input:
5
2 3 1 5

Output:
4
"""

def missingNumber(n, array):
    sumtotal = 0
    for i in range(len(array)):
        sumtotal += array[i]

    return n*(n+1)/2 - sumtotal

n = 5
array = [2, 3, 1, 5]
print(missingNumber(5, array))