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

# problem link: https://leetcode.com/problems/count-number-of-nice-subarrays/
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        s = 0
        ans = 0

        import collections
        d = collections.defaultdict(int)

        for c in nums:
            if c % 2: s += 1

            d[s] += 1

            if s == k: 
                ans += 1

            if s - k in d:
                ans += d[s-k]

        return ans

# question link: https://leetcode.com/discuss/interview-question/3114099/AMAZON-OA-(INTERN-2024)
import collections
d = collections.defaultdict(int)

s= 'mononom'
t = 'mon'

def targetword(s, t):
    ans = float('inf')
    for c in s:
        d[c] += 1
        
    for c in t:
        if d[c] > 0:
            ans = min(ans, d[c])
            d[c] -= 1
                
    return ans
    
print(targetword(s, t))

# problem link: https://www.desiqna.in/16114/visa-oa-sde-intern-ctc-30-lac-27th-oct
import collections
d = collections.defaultdict(int)

lamps = [[1,7],[5,11],[7,9]]
points = [7, 1, 5, 10, 9, 15]

p = [0] * 20
pt = []

def lampslight(s):
    ans = float('inf')
    for i in range(len(s)):
        for j in range(s[i][0], s[i][1]+1):
            p[j] += 1
    
    for k in range(len(points)):
        pt.append(p[points[k]])
        
    return pt

print(lampslight(lamps))

# problem link: https://www.desiqna.in/16189/backend-engineer-hackerrank-online-test
# need to revisit as 'k' is not used
events = ['Alex sleep 00:00 08:00', 'Sam sleep 07:00 13:00', 'Alex sleep 12:30 13:59']

t = []
booked = [0]* 23

import collections
d = collections.defaultdict(list)

def meetingassistant(events):
    for e in events:
        t.append((e.split(' ')[-2],e.split(' ')[-1]))
        
    for a in t:
        s_hour = int(a[0].split(':')[0])
        e_hour = int(a[1].split(':')[0])
        for i in range(s_hour, e_hour + 1): booked[i] += 1
    
    l = 0
    r = len(booked)
    
    while l < r:
        mid = l + (r - l)// 2
        
        if booked[mid] > 0:
            l = mid + 1
        else:
            r = mid
        
    return r if r < 25 else -1 

# question link: https://docs.google.com/document/d/1enINelZDWXi3ZLSLH5jbN-zXCzcWnrXFQ0RRUhJl6PY/edit
# count of shortest length subarrays with sum k
arr = [10,5,2,7,1,9,8,7,9,6]
k = 15

import collections
d = collections.defaultdict(int)

def shortestsubarray_cnt(arr,k):
    d[0] = -1
    s = 0
    mlen = float('inf')
    
    for i in range(len(arr)):
        s += arr[i]
        if s - k in d:
            mlen = min(mlen, i - d[s-k])
        d[s] = i
        
    # sliding window to find count of shortest length subarrays    
    i = 0
    j = 0
    cnt = 0
    
    s = 0
    while i <= j and j < len(arr):
        s += arr[j]
        
        if j - i + 1 < mlen:
            j += 1
        else:
            if s == k: cnt += 1
            s -= arr[i]
            i += 1
            j += 1
    
    return cnt
    
print(shortestsubarray_cnt(arr, k))

# question link: https://www.desiqna.in/15920/microsoft-oa-september-2023-freshers-hiring-sde1-set-115
# wrong submission
arr = [4,2,5,4,3,5,1,4,2,7]
x = 3
y = 2

# index issue
# arr = [10,3, 4,7]
# x = 2
# y = 3

prefix = [0] * (len(arr)-y-x+1)

def mincost_rehabs(arr, x, y):
    min_cost = float('inf')
    for i in range(1, len(arr)-y-x+1):
        j = i + y-1
        cnt = 1
        is_loop = False
        while cnt < x and j < len(arr):
            prefix[i] += arr[j]
            is_loop = True
            j += y
            cnt += 1
        if is_loop:prefix[i] += arr[i-1]
        min_cost = min(min_cost, prefix[i])
            
    return min_cost
    
print(mincost_rehabs(arr, x, y))

# question link: https://docs.google.com/document/d/11fn8ZwZ0Hr_-sdVJMMjKPHlFZAILhQ2nrd4eRSHEHDI/edit
prefix = [0] * 9

def maxlength(q):
    for i in range(len(q)):
        l = q[i][0]
        r = q[i][1]
        prefix[l] += 1
        if r + 1 < len(prefix): prefix[r+1] -= 1
        
    for i in range(len(prefix)):
        prefix[i] = prefix[i-1] + prefix[i]
        
    return prefix
    
q = [[1,8],[5,8]]
print(maxlength(q))

# question link: https://www.desiqna.in/16087/media-net-oa-sde1-ctc-28-l
arr = [5, -2, 3, 1, 2]
k = 3

prefix = [0] * (len(arr)+1)
suffix = [0] * (len(arr)+1)

# prefix[0] = arr[0]
suffix[len(arr)-1] = arr[-1]

def maxsumselection(arr,k):
    msum = 0
    for i in range(1, len(prefix)):
        prefix[i] = prefix[i-1] + arr[i-1]
        
    for i in range(len(suffix)-2, 0, -1):
        suffix[i-1] = suffix[i] + arr[i-1]

    for i in range(k):
        sidx = len(arr) - k + i + 1
        msum = max(msum, prefix[i+1] + suffix[sidx])

    return msum
    
print(maxsumselection(arr, k))

# https://docs.google.com/document/d/1HwqRB-dQZXKlHlpn-2KLqyrWDbYEZ4gD7uskSEQUUcM/edit
# need to revisit to convert to hashing - only one index pair is return , 3 idx exists as answer
arr = [5, 6, 7, 8, 10, 4, 3, 2, 1]
k = 8

import collections
d = collections.defaultdict(int)

def first_last_element_sum_shortest_subarray(arr,k):
    i = 0
    j = len(arr) - 1
    mlen = float('inf')
    while j >= i:
        s = arr[i] + arr[j]
        if s == k:
            mlen = min(mlen, j -i + 1)
        i += 1
        j -= 1

    return mlen
    
print(first_last_element_sum_shortest_subarray(arr, k))

# question link: https://docs.google.com/document/d/1LthiOPD4CvHTu9d0_h_XKJF9U9BYdjYYetnjjAPQLpo/edit
arr = [5,3,4,6,2,5]

prefix = [0] * len(arr)
suffix = [0] * len(arr)

def triplets(arr):
    for i in range(len(arr)-1):
        j = i + 1
        c = 0
        while j < len(arr):
            if arr[i] > arr[j]:
                c += 1
                
            j += 1
            
        prefix[i] = c
        
    for i in range(len(arr)-1, -1, -1):
        j = len(arr) - 1
        c = 0
        while j > i :
            if arr[j] > arr[i]:
                c += 1
                
            j -= 1
            
        suffix[i] = c
        
    c = 0
    # starting loop from 1..n as i < j and if j == 0 ; i does not exists
    for i in range(1, len(arr)):
        c += prefix[i] * suffix[i]
        
    return c
    
print(triplets(arr))

# question link: https://www.geeksforgeeks.org/count-quadruplets-with-sum-k-from-given-array/
# wrong submission
arr = [4, 5, 3, 1, 2, 4]
tsum = 13

# 5 3 4 1
# 1 5 3 4
# 5 3 2 3
# 5 4 1 3

import collections
d = collections.defaultdict(list)

def quadruplets_sum_k(arr, k):
    cnt = 0
    for i in range(len(arr)-1):
        j = i + 1
        s = arr[i]
        while j < len(arr):
            s += arr[j]
            d[s].append((i,j))
            s -= arr[j]
            j += 1
            
    
    for i in range(len(arr)-1):
        j = i + 1
        s = arr[i]
        while j < len(arr):
            s += arr[j]
            temp = k - s
            if temp in d and all((i,j) > (x,y) for x,y in d[temp]): 
                cnt += 1
            s -= arr[j]
            j += 1
            
    return cnt
    
print(quadruplets_sum_k(arr, tsum))

# question link: https://www.desiqna.in/15068/google-oa-swe-intern-july-2023-solution-by-kumar-k

arr = [1, 2, 6,6, 5]

import collections
d = collections.defaultdict(list)

def max_pairs(arr):
    for i in range(len(arr)-1):
        j = i + 1
        while j < len(arr):
            s = arr[i] + arr[j]
            if (arr[i], arr[j]) not in d[s]:
                d[s].append((arr[i], arr[j]))
            j += 1
        
    mx = 0   
    s = 0
    for k, v in d.items():
        if mx < len(v):
            s = k
            mx = len(v)
            
    return d[s]
    
print(max_pairs(arr))

# question link: https://docs.google.com/document/d/19QBr6ahoVh3himYXB6Fd0JscC6yhjV9qLyt2fGpdLhk/edit

arr = [5, 8, -100, 2, 3, 4]

prefix = [0] * len(arr)
suffix = [0] * len(arr)

prefix[0] = arr[0]
suffix[-1] = arr[-1]

def max_sum_non_overlapping(arr):
    mx = 0
    for i in range(1, len(arr)):
        prefix[i] = max(arr[i], prefix[i-1]+ arr[i])
        
    for i in range(len(arr)-2, -1, -1):
        suffix[i] = max(arr[i], suffix[i+1]+ arr[i])

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            mx = max(mx, prefix[i] + suffix[j])
    
    return mx
    
print(max_sum_non_overlapping(arr))

# question link: https://www.desiqna.in/15839/zscaler-oa-2023-sep-set-10
arr = [9, 3, 1, 2, 3, 9, 10, 0, 3, 2, 1, 3]

prefix = [0] * (len(arr))
prefix[0] = arr[0]

for i in range(1,len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

def first_last_number(arr):
    cnt = 0
    for i in range(len(arr)-1):
        j = len(arr) -1
        while i < j:
            if arr[i] != arr[j]:
                j -= 1
            else:
                s = prefix[j-1] - prefix[i] 
                if s == arr[i]: cnt += 1
                j -= 1
    
    return cnt
    
print(first_last_number(arr))

# question link: https://docs.google.com/document/d/1Y64Xw5WeW6-UYXXuu75_w7_AQU9tlqYdvhGfHc7-XqU/edit
arr = [1, 8, 10,8, -5, 8, 9, 9, 9, 9, 9, 10]

prefix = [0] * len(arr)
prefix[0] = arr[0]

def max_sum_subarray_first_last_elem_equal(arr):
    mx = 0
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
        
            
    for i in range(len(arr)-1):
        j = len(arr) - 1
        while i < j:
            if arr[i] != arr[j]:
                j -= 1
            else:
                s = prefix[j] - prefix[i-1]
                if mx < s: mx = s
                j -= 1
                
    return mx

print(max_sum_subarray_first_last_elem_equal(arr))