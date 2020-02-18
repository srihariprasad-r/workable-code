"""
Input : [0,2,1,0,0,1,2,2,1]
Output: [0,0,0,1,1,1,2,2,2]
"""

def sortnonbinaryarray(array):
    count0 = array.count(0)
    count1 = array.count(1)
    count2 = array.count(2)
    k = 0
    newarray = []

    while(count0 != 0):
        newarray.append(0)
        k += 1
        count0 -= 1

    while(count1 != 0):
        newarray.append(1)
        k += 1
        count1 -= 1

    while(count2 != 0):
        newarray.append(2)
        k += 1
        count2 -= 1

    return newarray

array = [0,2,1,0,0,1,2,2,1]
sortnonbinaryarray(array)