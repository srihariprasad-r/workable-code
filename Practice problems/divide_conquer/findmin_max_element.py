def findmaxmin(arr, low, high, minel=float('inf'), maxel=-float('inf')):
    if low == high:             # only one element
        if minel > arr[high]:
            minel = arr[high]
        
        if maxel < arr[low]:
            maxel = arr[low]
        
        return minel, maxel
            
    if high - low == 1:             #only two element exists
        if arr[low] < arr[high]:
            if minel > arr[low]:
                minel = arr[low]
            else:
                if maxel < arr[high]:
                    maxel = arr[high]
        else:
            if minel > arr[high]:
                minel = arr[high]
            else:
                if maxel < arr[low]:
                    maxel = arr[low]
        
        return minel, maxel
                    
    mid = low + (high-low) //2
    
    minel, maxel = findmaxmin(arr, low, mid, minel, maxel)
    
    minel, maxel = findmaxmin(arr, mid+1, high, minel, maxel)
    
    return minel, maxel
    
arr = [5, 7, 2, 4, 9, 6]
print(findmaxmin(arr, 0, len(arr)-1))