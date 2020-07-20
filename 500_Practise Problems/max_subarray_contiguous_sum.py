"""
Given array of integers, find the maximum contiguous sum
"""

def maxContiguousSum(arr):
  maxSum = arr[0]
  maxContSum = arr[0]
  index_list = []
  for i in range(1, len(arr)):
    maxSum = max(maxSum+arr[i], arr[i])
    maxContSum = max(maxSum, maxContSum)
  
  print(maxContSum)

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxContiguousSum(arr)
