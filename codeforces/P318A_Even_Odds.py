import math

arr = [int(x) for x in input().split()]

n = arr[0]
k = arr[1]

median = math.ceil(n/2)

if k <= median:
    print(2*k -1)
else:
    print((k - median) * 2)




    