def lscs(arr):
    max_so_far = 0
    maxval = 0
    start = 0
    end = 0

    for i in range(len(arr)):
        maxval = maxval + arr[i]

        if maxval < 0:
            maxval = 0
            start = i+1
        
        if max_so_far < maxval:
            max_so_far = maxval
            end = i

    return arr[start: end + 1]

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(lscs(arr))