"""Given unsorted array, find pair with given sum in it.

Input = [8,7,2,5,3,1]
sum = 10

Output:

Pair at index 0 & 2 -> (8,2)
Pair at index 1 & 4 -> (7,3)
"""

def sum_given_pair(array, sum):
    low = 0
    high = len(array) - 1

    while (low < high):
        if array[low] + array[high] == sum:
            return (low, high)
        elif array[low] + array[high] < sum:
            low += 1
            high -=  1
        else:
            return False

array = [8,7,2,5,3,1]
output = sum_given_pair(array, 10)     
print(output)