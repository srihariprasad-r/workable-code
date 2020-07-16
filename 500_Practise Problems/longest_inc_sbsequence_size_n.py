"""Find longest increasing subsequence with size n and O(n)= nlogn
"""

A = [1, 3, 4, 2]

def CeilIndex(A, l, r, key): 
    while (r - l > 1): 
        m = l + (r - l)//2
        if (A[m] >= key): 
            r = m 
        else: 
            l = m 
    return r 

def increasingsequence(A):
  c = 1
  temp = [1 for _ in range(len(A))]
  
  temp[0] = A[0]
  for i in range(len(A)):
    if A[i] < temp[0]:
      temp[0] = A[i]
    elif A[i] > temp[c-1]:
      temp[c] = A[i]
      c += 1
    else:
      temp[CeilIndex(A, -1, c-1, A[i])]= A[i]
  
  return c
  
print(increasingsequence(A))