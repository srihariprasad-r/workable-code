"""
Bubble sort assumes that if there are n elements, and if n -1 is sorted, then nth element will be sorted

So, first loop goes to n -1 iteration
  - For each iteration, j will run from 0 to len(arr) - i, as ith element is assumed to be sorted
  - if elements at index j+1 < j, swap them

"""
def bubblesort(arr):
    for i in range(1,len(arr)):
        for j in range(len(arr)-i):
            if arr[j+1] < arr[j]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr
                


arr = [5, 2, 8, 9, 1]
print(bubblesort(arr))