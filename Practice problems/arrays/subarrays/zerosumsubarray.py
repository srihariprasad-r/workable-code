def zerosumsubarray(arr):
    if len(arr) == 0:
        return False
        
    s = set()
    s.add(0)
    sum = 0
    
    for n in arr:
        sum += n
        
        if sum in s:
            return True
            
        s.add(sum)
        
    return False
    
arr = [4, -6, 3, -1, 4, 2, 7]
print(zerosumsubarray(arr))