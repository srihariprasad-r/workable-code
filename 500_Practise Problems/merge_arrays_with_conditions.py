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
    newcount = count        #this variable is used to capture count of non-zero elements in the list

    while(count < len(x)):
        x[count] = 0
        count += 1
    return x, y, newcount


def mergesort(x, y, count):

    m = count - 1
    n = len(y) - 1
    k = m + n + 1

    while (m >= 0 and n >= 0):
        if x[m] > y[n]:
            x[k] = x[m]
            m -= 1
        else:
            x[k] = y[n]
            n -= 1
        k -= 1
    
    while n >= 0:
        x[k] = y[n]
        n -= 1
        k -= 1

    for i in range(len(y)):
        y[i] = 0

    return x, y 

x = [0,2,0,3,0,5,6,0,0]
y = [1,8,9,10,15]

new_x, y, nonzero_count = rearrange(x,y)
upd_x, upd_y = mergesort(new_x, y, nonzero_count)
print(upd_x, upd_y)
