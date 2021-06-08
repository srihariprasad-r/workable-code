def spiralmatrix(arr):
    minrow, mincol = 0, 0 
    maxrow, maxcol = len(arr) - 1, len(arr[0]) -1
    n, m = len(arr) , len(arr[0])
    tne = n * m
    cnt = 0 
    
    while cnt < tne:
        for j in range(mincol,maxcol+1):
            if cnt < tne:
                i = minrow
                print(arr[i][j])
                cnt += 1
        minrow += 1
        for i in range(minrow, maxrow+1):
            if cnt < tne:
                j = maxcol
                print(arr[i][j])
                cnt += 1
        maxcol -= 1  
        for j in range(maxcol, mincol-1, -1):
            if cnt < tne:
                i = maxrow
                print(arr[i][j])
                cnt += 1
        maxrow -= 1 
        for i in range(maxrow, minrow-1, -1):
            if cnt < tne:
                j = mincol
                print(arr[i][j])
                cnt += 1
        mincol += 1 

arr = [
    [1, 2, 3, 4],
    [2, 40,50, 6],
    [4, 5, 6, 7],
    [4, 50, 5, 8]
]
print(spiralmatrix(arr))