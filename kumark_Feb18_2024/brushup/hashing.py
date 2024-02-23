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
        
# minimum operations to make array equal

arr = [1, 2, 3,4]

def brute(arr):
    max_freq = 0
    for i in range(len(arr)):
        curr_freq = 1
        for j in range(i):
            if arr[i] == arr[j]:
                curr_freq += 1
                
        if curr_freq > max_freq:
            max_freq = curr_freq

                    
    return len(arr) - max_freq
                    
                    
# print(brute(arr))

import collections
a = {}
def hashing(arr):
    mx = 0
    for i in range(len(arr)):
        if arr[i] not in a:
            a[arr[i]] = 1
        else:
            a[arr[i]] += 1
        
        mx = max(mx, a[arr[i]])
        
    return len(arr) - mx
        
    
print(hashing(arr))

# two sum

arr = [3,4,6,5,8,2,1]
tgt = 14

import collections

d = collections.defaultdict(int)
d[0] = [-1]

def twosum(arr):
    for idx, x in enumerate(arr):
        if abs(x -tgt) in d:
            othervalue = d[abs(x-tgt)]
            return [idx, othervalue]
        else:
            d[x] = idx
        
print(twosum(arr))