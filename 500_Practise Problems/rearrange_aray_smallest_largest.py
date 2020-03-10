"""
Print the array in the order – smallest number, Largest number, 2nd smallest number, 2nd largest number, 
3rd smallest number, 3rd largest number and so on….

Input = [5, 8, 1, 4, 2, 9, 3, 7, 6]

Output = {1, 9, 2, 8, 3, 7, 4, 6, 5}
"""

def arrayarrange(array):
    new_array = []
    array = sorted(array)
    index = 0
    i = 0
    j = len(array)-1
    n = len(array)

    while (i <= n//2 or j > n//2):
        new_array.insert(index, array[i])
        index += 1
        new_array.insert(index, array[j])
        index += 1
        i += 1
        j -= 1
        
    print(new_array)

array = [5, 8, 1, 4, 2, 9, 3, 7, 6]
arrayarrange(array)