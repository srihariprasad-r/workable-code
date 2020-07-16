"""
Generate all subarrays of an array
"""

def generatesubarray(array, start, end):
  if end == len(array):
    return
  elif start > end:
    generatesubarray(array, 0, end +1)
  else:
    print(array[start:end+1])
    generatesubarray(array, start +1 , end)

A = [1, 2, 3, 4]
generatesubarray(A, 0 , 0)
