"""
Given array of length n, find maximum sum of subarray of length k
"""


def maximumSubarraySum(A, k):
  n = len(A)
  window_sum = sum(A[:k])
  maxSum = 0
  for i in range(n-k):
    window_sum = window_sum - A[i] + A[i+k]
    maxSum = max(maxSum, window_sum)
  
  print(maxSum)

A = [1, 2, 3, 4]
maximumSubarraySum(A, 3)