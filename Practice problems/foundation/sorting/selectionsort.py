"""
Selection sort assumes that if there are n elements, and if n -1 is sorted, then nth element will be sorted

So, first loop goes to n -1 iteration
  - assign i as min element
  - For each iteration, j will run from 0 to len(arr)
  - if elements at index min > j, swap them at end of each iteration

"""

def selectionsort(arr):
    for i in range(len(arr)):
        min = i
        j = i + 1
        
        while j < len(arr):
            if arr[j] < arr[min]:
                min = j
                
            j += 1
            
        if min != i :
            temp = arr[min]
            arr[min] = arr[i]
            arr[i] = temp
    
    return arr
                


arr = [5, 2, 8, 9, 1]
print(selectionsort(arr))