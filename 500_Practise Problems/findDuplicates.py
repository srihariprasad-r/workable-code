"""
Find duplicate element in given array
Input = [1,2,3,4,4]

Output = 4

"""

def findDuplicates(array):
    visited_list = [False]* (len(array))

    for i in range(len(array)):
        if visited_list[array[i]]:
            return array[i]

        visited_list[array[i]] = True
    
    return -1

array = [1,2,3,4,4]
a = findDuplicates(array)
print(a)
