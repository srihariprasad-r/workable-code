"""
Perform merge sort by merging elements of Y to correct order in X
Input:

X = [0,2,0,3,0,5,6,0,0]
Y= [1,8,9,10,15]

Output:

X = [1,2,3,5,6,8,9,10,15]
"""

def rearrange(x, y):
    count = 0
    for i in range(len(x)):
        if x[i] != 0:
            x[count] = x[i]
            count += 1
        
    while(count < len(x)):
        x[count] = 0
        count += 1
    print(count)
    return x, y 


def mergesort(x, y):
    m = len(x)
    n = len(y)
    i = 0 
    j = 0
    k = 0

    while (i < m and j < n):
        if x[i] > y[j]:
            x[k] = y[j]
            j += 1
        else:
            i += 1
        k += 1
    
    while n <= 0:
        x[k] = y[n]
        n -= 1

    print(x)

x = [0,2,0,3,0,5,6,0,0]
y = [1,8,9,10,15]

new_x, y = rearrange(x,y)
mergesort(new_x, y)
