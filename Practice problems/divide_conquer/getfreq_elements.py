def getfreq(arr, low, high, freq_dct={}):
    if low == high:
        return
    
    if arr[low] == arr[high]:
        cnt = freq_dct.get(arr[low], None)
        if cnt is None:
            cnt = 0
        freq_dct[arr[low]] = cnt + high - low + 1 
            
        return
    
    mid = low + (high - low)//2
    
    getfreq(arr, low, mid, freq_dct)
    getfreq(arr, mid+1, high, freq_dct)
    
    return freq_dct
    
arr = [2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9]
print(getfreq(arr, 0, len(arr)-1))