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