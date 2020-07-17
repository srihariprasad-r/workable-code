"""
Given an array and an integer K, find the maximum for each and every contiguous subarray of size k
"""

def slidingWindowMaxNum(A, k):
  for i in range(len(A)-k+1):    
    maxNum = A[i]
    #print(maxNum)
    for j in range(1,k):
      if A[i+j] > maxNum:
        maxNum = A[i+j]
    print(maxNum, end=" ")


A = [1, 2, 3, 4]
slidingWindowMaxNum(A, 3)