import sys

arr = [12, 13, 1, 10, 34, 1] 

def smallest_second_smallest(arr):
    first = second = sys.maxint
    
    for i in range(len(arr)):
        if arr[i] < first:
            second = first
            first = arr[i]
        elif (arr[i] > first and second > arr[i]):
            second = arr[i]
    print(first, second)
    
smallest_second_smallest(arr)
    
