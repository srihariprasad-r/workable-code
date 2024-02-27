# question link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# wrong submission
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2: return [-1,-1]
        def firstpos(arr, k):
            l = 0
            r = len(arr) - 1
            
            while l < r:
                mid = l + (r-l)//2
  
                if arr[mid] == k: return mid
                
                if arr[mid] > k:
                    r = mid - 1
                else:
                    l = mid + 1
                    
            return -1 if arr[l] != k else l

        def lastpos(arr, k):
            l = 0
            r = len(arr) - 1
            
            while l < r:
                mid = l + (r-l)//2

                if arr[mid] == k: return mid
                
                if arr[mid] > k:
                    r = mid
                else:
                    l = mid + 1
                    
            return -1 if arr[r] != k else r

        return [firstpos(nums, target), lastpos(nums, target)]