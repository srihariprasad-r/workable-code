def rotate_matrix(arr):
    n = len(arr)
    rows = len(arr)
    cols = len(arr[0])
    
    midrow = len(arr)//2 
    
    for j in range(cols//2):
        tmp = arr[midrow][j]
        arr[midrow][j] = arr[midrow][n-j-1]
        arr[midrow][n-j-1] = tmp
        
    
    for i in range(rows//2+1):
        for j in range(cols):
            tmp = arr[i][j]
            arr[i][j] = arr[n-i-1][n-j-1]
            arr[n-i-1][n-j-1] = tmp
            
    return arr


arr =  [ 
    [ 1, 2, 3, 4, 5 ],
    [ 6, 7, 8, 9, 10 ],
    [ 11, 12, 13, 14, 15 ],
    [ 16, 17, 18, 19, 20 ],
    [ 21, 22, 23, 24, 25 ] 
]
print(rotate_matrix(arr))  
# [25, 24, 23, 22, 21], [20, 19, 18, 17, 16], [15, 14, 13, 12, 11], [10, 9, 8, 7, 6], [5, 4, 3, 2, 1]]