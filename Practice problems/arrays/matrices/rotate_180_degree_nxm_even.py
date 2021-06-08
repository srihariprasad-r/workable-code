def rotate_matrix(arr):
    n = len(arr)
    rows = len(arr)
    cols = len(arr[0])
    
    for j in range(cols//2-1,cols//2):
        for i in range(rows):
            tmp = arr[j][i]
            arr[j][i] = arr[n-j-1][n-i-1]
            arr[n-j-1][n-i-1] = tmp
        
    
    for i in range(rows//2+1):
        for j in range(cols):
            tmp = arr[i][j]
            arr[i][j] = arr[n-i-1][n-j-1]
            arr[n-i-1][n-j-1] = tmp
    
    return arr


arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(rotate_matrix(arr))  # [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]