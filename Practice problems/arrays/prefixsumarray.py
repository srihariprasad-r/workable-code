def prefixsumarray(arr):
    prefix_array = [0]*len(arr)
    prefix_array[0] = arr[0]
    for i in range(1, len(arr)):
        start = 0
        while start <= i:
            prefix_array[i] = prefix_array[i-1] + arr[start]
            start += 1
    
    print(prefix_array)

arr = [10, 20, 10, 5, 15]
prefixsumarray(arr)