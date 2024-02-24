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

# prefix sum
arr = [2,4,3,1,6,5,7,3,2]
l = 4
r = 5

prefix = [0]*(len(arr)+1)


def psum(arr, l, r):
    for idx in range(1,len(prefix)):
        prefix[idx] = prefix[idx-1] + arr[idx-1]
        
    return prefix[r] - prefix[l-1]
        
print(psum(arr,l,r))

# subarray sum < k

arr = [2,4,-3,2,5,-1,2]
k = 3

prefix = [0]*(len(arr)+1)

import collections
d = collections.defaultdict(int)
d[0] = 1

def subarraysum(arr,k):
    c = 0
    for idx in range(1,len(prefix)):
        prefix[idx] = prefix[idx-1] + arr[idx-1]
    
    for i in range(1,len(prefix)):
        if prefix[i] - k in d:
            d[prefix[i] - k] += 1
            c += 1
        else:
            d[prefix[i]] = 1
            
    return c
        
print(subarraysum(arr,k))

# longest consective sequence
nums = [0,3,7,2,5,8,4,6,0,1]


def longest_sequence(arr):
    c = 0

    for a in arr:
        l = 0
        if a - 1 not in nums:
            while a + l in nums:
                l += 1
            c = max(c, l)
        
    return c

print(longest_sequence(nums))