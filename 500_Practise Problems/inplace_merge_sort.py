"""
Perform inplace merge sort(without additional array)
Input:

X = [1,4,7,8,10]
Y= [2, 3, 9]

Output:

X = [1,2,3,4,7]
Y= [8, 9, 10]
"""

def inplaceMergeSort(x, y):
    i = len(x)
    j = len(y)

    k = 1

    for i in range(len(x)):
        if x[i] > y[0]:
            first_y = y[0]
            x[i], y[0] = y[0], x[i]

            #moved it inside if clause as it is throwing index out of range exception
            while k < j and y[j] < first_y:
                y[j - 1] = y[j]
                y[j] = first_y
                k += 1
    
    return x, y

x = [1,2,3,4,7]
y = [8, 9, 10]

output_x, output_y = inplaceMergeSort(x, y)
print(output_x, output_y)

