"""
Wave traversal is first go top to bottom, for next column go from bottom to top and continue
[
   | 1 | 2 | 3
   | 4 | 5 | 6
]

To achieve this, for even columns, we go top to bottom and vice-versa for odd columns
"""

def wavetraversal(arr1):
    r1, c1 = len(arr1), len(arr1[0])

    for i in range(len(arr1[0])):
        if i % 2 == 0:
            for j in range(len(arr1)):
                print(arr1[j][i])
        else:
            for j in range(len(arr1) -1, -1, -1):
                print(arr1[j][i])
        


arr1 = [
    [1, 2, 3],
    [4, 5, 6]
]

print(wavetraversal(arr1))