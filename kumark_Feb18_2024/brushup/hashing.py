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

# two sum
# question link: https://www.geeksforgeeks.org/check-if-pair-with-given-sum-exists-in-array/
arr = [0, -1, 2, -3, 1]
v = -2

import collections
d = collections.defaultdict(int)

def sumarray(t):
    for i in range(len(arr)):
        if t - arr[i] in d:
            return True
        else:
            d[arr[i]] = 1
            
    return False
    
print(sumarray(v))

# question link : https://www.geeksforgeeks.org/find-whether-an-array-is-subset-of-another-array-set-1/
arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]

import collections
d = collections.defaultdict(int)

def subsetarray(arr1, arr2):
    for i in range(len(arr1)):
        d[arr1[i]] = 1
        
    for j in range(len(arr2)):
        if not (arr2[j] in d):
            return False
            
    return True
    
print(subsetarray(arr1, arr2))

# question link: https://www.geeksforgeeks.org/maximum-distance-two-occurrences-element-array/
arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]

import collections
d = collections.defaultdict(list)

def maxdistance(arr):
    mx = 0
    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]].append(i)
        else:
            cnt = len(d[arr[i]]) 
            if cnt > 1:
                while cnt > 1:
                    d[arr[i]].pop()
                    d[arr[i]].append(i)
                    cnt -= 1
            else:
                d[arr[i]].append(i)

    for b in d.values():
        if len(b) > 1: mx = max(mx, b[1]-b[0])
            
    return mx
    
print(maxdistance(arr))

# question link: https://www.geeksforgeeks.org/sum-of-elements-in-an-array-with-frequencies-greater-than-or-equal-to-that-element/?ref=rp
arr = [2, 1, 1, 2, 1, 6]

import collections
d = collections.defaultdict(int)

def sumfrequency(arr):
    mx = 0
    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]] =  1
        else:
             d[arr[i]] += 1

    for k, v in d.items():
        if v >= k:
            mx += k
            
    return mx
    
print(sumfrequency(arr))

# question link: https://leetcode.com/problems/first-unique-character-in-a-string/
s = "loveleetcode"

import collections
d = collections.defaultdict(int)

def uniquechar(s):
    mx = float('inf')
    st = set()
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] =  i
        else:
             d[s[i]] += 1
             st.add(s[i])

    for k, v in d.items():
        if not(k in st):
            mx = min(mx, d[k])
            
    return mx
    
print(uniquechar(s))

# question link: https://leetcode.com/problems/find-common-characters/
words = ["bella","label","roller"]

def commonchars(words):
    chr_array = [float('inf')] * 26
    res = []
    
    for s in words:
        s_array = [0] * 26
        for c in s:
            s_array[ord(c)-ord('a')] += 1
            
        for idx, v in enumerate(s_array):
            chr_array[idx] = min(s_array[idx], chr_array[idx])
            
    for idx, c in enumerate(chr_array):
        while c > 0:
            res.append(chr(idx + ord('a')))
            c -= 1
        
    return res
        
print(commonchars(words))

# question link: https://www.geeksforgeeks.org/count-pairs-with-given-sum/
arr = [1, 5, 7, -1, 5]
k = 6

import collections
d = collections.defaultdict(int)

def countpairs(arr, k):
    res = 0
    for c in arr:
        if abs(c - k) in d:
            res += 1
        else:
            d[c] += 1
    
    return res
            
print(countpairs(arr,k))