# search rotated array

arr = [0, 1,2,4,5,6,7]
tgt = 1

def searcharray(arr,tgt):
    l = 0 
    r = len(arr) - 1
    
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] == tgt:
            return mid
            
        if arr[l] <= arr[mid]:
            if tgt < arr[l] or tgt > arr[mid]:
                l = mid + 1
            else:
                r = mid
        else:
            if tgt <= arr[mid] or tgt >= arr[r]:
                r = mid
            else:
                l = mid +1
            
    return -1
    
print(searcharray(arr,tgt))

# single element

arr = [3,3,7,7,10,11,11]

def single_element(arr):
    l = 0 
    r = len(arr) - 1
    
    while l <= r:
        mid = l + (r-l+1)//2

        if arr[mid-1] != arr[mid] and arr[mid] != arr[mid+1]:
            return mid
        
        if mid % 2:
            if arr[mid] == arr[mid-1]:
                l = mid + 1
            else:
                r = mid - 1
        else :
            if arr[mid] == arr[mid+1]:  
                r = mid - 1
            else:
                l = mid + 1

    
print(single_element(arr))