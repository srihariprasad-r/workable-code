"""
Given array of integers, find the maximum contiguous sum
"""

def maxContiguousSum(arr):
  maxSum = arr[0]
  maxContSum = arr[0]
  start = 0
  end = 0
  
  for i in range(1, len(arr)):
    #running sum
    maxSum = max(maxSum+arr[i], arr[i])
    #if sum is less than 0, shift pointer to next element
    if maxSum <0 :
      start = i+1      
    elif maxSum > maxContSum:
      end = i 
    #reassign the correct max sum  
    maxContSum = max(maxSum, maxContSum)    

  return start, end, maxSum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxContiguousSum(arr))