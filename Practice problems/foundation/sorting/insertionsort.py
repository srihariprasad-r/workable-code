"""
Insertion sort assumes that if there are n elements, and if n -1 is sorted, then nth element will be sorted

So, first loop goes to n -1 iteration
  - assign i as sorted element
  - For each iteration, j will run from i+1 to len(arr)
  - if elements at index sorted > j, swap them at end of each iteration
"""

def insertionsort(arr):
    for i in range(1, len(arr)):
        sorted = i - 1
        j = i
        
        if arr[j] > arr[sorted]:
            continue
        else:
            while j >= 1 and arr[j-1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
                j -= 1

    return arr


arr = [5, 1, 9, 2, 8]
print(insertionsort(arr))
