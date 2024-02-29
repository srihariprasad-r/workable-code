# question link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums, target):
        if not nums: return [-1,-1]
        if len(nums) == 1: 
            if nums[-1] == target: return [0,0]
            else: return [-1,-1]
        
        def firstpos(arr, k):
            l = 0
            r = len(arr) - 1
            
            while l < r:
                mid = l + (r-l)//2

                if arr[mid] < k:
                    l = mid + 1
                else:
                    r = mid

            return -1 if arr[l] != k else l
            
        def lastpos(arr, k):
            l = 0
            r = len(arr)
            
            while l < r:
                mid = l + (r-l)//2
 
                if arr[mid] > k:
                    r = mid
                else:
                    l = mid + 1

            return -1 if arr[r-1] != k else r - 1

        return [firstpos(nums, target), lastpos(nums, target)]

# question link: https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, arr, target):
        l = 0
        r = len(arr)

        while l < r:
            mid = l + (r - l) // 2

            if arr[mid] == target:
                return mid

            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l      

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