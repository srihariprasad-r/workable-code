"""
Given an array and an integer K, find the maximum for each and every contiguous subarray of size k
"""

#Method 1:

def slidingWindowMaxNum1(A, k):
  for i in range(len(A)-k+1):    
    maxNum = A[i]
    #print(maxNum)
    for j in range(1,k):
      if A[i+j] > maxNum:
        maxNum = A[i+j]
    print(maxNum, end=" ")


#A = [1, 2, 3, 4]
#slidingWindowMaxNum1(A, 3)


#Method 2:

def slidingWindowMaxNum2(A, k):
  p = 0
  n = len(A)
  q = k - 1 
  t = p
  maxNum = A[k-1]

  while(q <= n -1):
    if(A[p] > maxNum):
      maxNum = A[p]
    p += 1
    
    if (q == p and p != n):
      print(maxNum, end=" ")
      q += 1
      p = t + 1
      t = p

      if (q < n):
        maxNum = A[q]

A = [1, 2, 3, 4]
slidingWindowMaxNum2(A, 3)