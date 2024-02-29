# hashing roadmap: https://www.desiqna.in/4678/best-roadmap-prepare-hashing-coding-interviews-kumar-desiqna


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

# question link: www.geeksforgeeks.org/number-subarrays-sum-exactly-equal-k
arr = [7,-3,3,-5,4,-2,-1,1]
k = 4

import collections

prefix = [0] * (len(arr) + 1)
d = collections.defaultdict(int)

def subarraysum(arr, k):
    cnt = 0
    for i in range(1,len(prefix)):
        prefix[i] = prefix[i-1] + arr[i-1]
        
    for i in range(1, len(prefix)):
        if prefix[i] == k:
            cnt += 1
            
        if prefix[i]-k in d:
            cnt += d[prefix[i]-k]
            
        d[prefix[i]] += 1
        
    return cnt
    
print(subarraysum(arr, k))

# question link: https://stackoverflow.com/questions/64418218/smallest-subarray-with-sum-equal-to-k
arr = [2, 4, 6, 10, 2, 1]
k = 12

import collections

prefix = [0] * (len(arr) + 1)
d = collections.defaultdict(int)

def smallestlengthsubarray(arr, k):
    cnt = float('inf')
    for i in range(1,len(prefix)):
        prefix[i] = prefix[i-1] + arr[i-1]
        
    print(prefix)
        
    for i in range(1, len(prefix)-1):
        j = 0
        while j < i:
            diff = prefix[i] - prefix[j]
            if diff == k:
                cnt = min(cnt, i -j)
            j += 1
        
    return cnt
    
print(smallestlengthsubarray(arr, k))

# question link: https://www.geeksforgeeks.org/count-number-subarrays-given-xor/
arr = [4, 2, 2, 6, 4]
k = 6

import collections

prefix = [0] * (len(arr)+1)
d = collections.defaultdict(int)


def bitwise_xor_subarrays(arr, k):
    cnt = 0
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] ^ arr[i-1]
        
    for i in range(1, len(prefix)):
        if prefix[i] == k:
            cnt += 1
    
        if prefix[i] ^ k in d:
            cnt += d[prefix[i]^k]
            
        d[prefix[i]] += 1
        
    return cnt 
    
print(bitwise_xor_subarrays(arr, k))

# question link: https://leetcode.com/contest/biweekly-contest-103/problems/find-the-prefix-common-array-of-two-arrays/
A = [2,3,1]
B = [3,1,2]
C = [0] * len(A)

import collections

d = collections.defaultdict(list)

def prefixcommon(arr1, arr2):
    for idx, x in enumerate(arr1):
        c = idx
        while c > -1:
            d[idx].append(arr1[c])
            c -= 1
            
    for i in range(len(arr2)):
        ct = 0
        for j in range(i+1):
            if arr2[j] in d[i]:
                ct += 1
        C[i] = ct
    
    return C   
    
print(prefixcommon(A, B))

# question link: www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809
A = [10, 5, 2, 7, 1, 9]
k = 15

prefix = [0] * (len(A)+1)

import collections

d = collections.defaultdict(list)

def longestsubarraysum(arr1):
    mx = float('-inf')
    for idx in range(len(arr1)):
        prefix[idx] = prefix[idx-1] + A[idx-1]
            
    for i in range(1, len(prefix)):
        j = 0
        s = 0
        while j < i:
            s = prefix[i] - prefix[j]
            if s == k:
                mx = max(mx, i - j)
            j += 1
    
    return mx  
    
print(longestsubarraysum(A))

# question link: https://www.desiqna.in/13267/microsoft-coding-oa-sde-1-may-3-2023
arr = [51, 32, 43]

import collections
d = collections.defaultdict(int)

def digitsum(s):
    m = 0
    
    while s > 0:
        m += s % 10
        s = s // 10
        
    return m

def solution(arr):
    mx = float('-inf')
    for i in range(len(arr)):
        f = digitsum(arr[i])
        if f in d:
            mx = max(mx, arr[i] + d[f])
        else:
            d[f] = arr[i]
        
    return mx if mx != float('-inf') else -1
    
print(solution(arr))