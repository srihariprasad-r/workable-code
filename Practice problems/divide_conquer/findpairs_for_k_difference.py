def binarysearch(A, val):
    low = 0
    high = len(A) - 1
    
    while low <= high:
        if A[low] == val:
            return low
            
        mid = low + (high-low)//2
        
        if A[mid] > val:
            high = mid - 1
        elif A[mid] < val:
            low = mid + 1
        else:
            return mid
            
    return -1

def findpairs(arr, tgt):
    arr.sort()
    
    i = 0
    
    while i < len(arr):
        while i < len(arr) - 1 and arr[i] == arr[i+1]:
            i += 1
        
        if binarysearch(arr, arr[i]-tgt) >= 0:
            print((arr[i], arr[i]-tgt))
            
        i += 1
    
arr = [1, 5, 2, 2, 2, 5, 5, 4]
print(findpairs(arr, 3))
