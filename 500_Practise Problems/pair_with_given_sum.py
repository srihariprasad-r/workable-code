"""
Input = {11, 15, 6, 8, 9, 10}
X = 16

Output = (6,10)
"""

def pairwithgivensum(array,x):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if (array[i] + array[j] == x and i !=j):
                return (i, j)
    
    return False


array = [11, 15, 26, 38, 9, 10]
output = pairwithgivensum(array, x=35)
print(output)