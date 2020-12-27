def maximumtripletsum(arr):
    max_A = -float('inf')
    max_B = -float('inf')
    max_C = -float('inf')

    for i in range(len(arr)):
        if arr[i] > max_A:
            max_C = max_B
            max_B = max_A
            max_A = arr[i]
        elif arr[i] > max_B:
            max_C = max_B
            max_B = arr[i]
        else:
            max_C = arr[i]
    
    return [max_A, max_B, max_C]

arr = [ 1, 0, 8, 6, 4, 2 ] 
print(maximumtripletsum(arr))