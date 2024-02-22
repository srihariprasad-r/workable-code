# check if duplicate is present at distance k 

arr = [1, 2, 3, 1, 2, 3, 4]
k = 3

def brute(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                if j -i <= k: return True
                    
    return False
                    
                    
# print(brute(arr))

import collections
a = {}
def hashing(arr):
    for i in range(len(arr)):
        if arr[i] not in a:
            a[arr[i]] = i
        else:
            if i - a[arr[i]] <= k: 
                return True
            a[arr[i]] = i
    
    return False
        
    
print(hashing(arr))
        