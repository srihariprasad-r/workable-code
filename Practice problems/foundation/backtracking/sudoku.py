def isvalid(arr, x, y, value):
    for i in range(len(arr)):
        if arr[i][y] == value:
            return False
    
    for j in range(len(arr[0])):
        if arr[x][j] == value:
            return False
        
    submatrix_i = 3 * (x//3)
    submatrix_j = 3 * (y//3)
    for k in range(3):
        for n in range(3):
            if arr[submatrix_i+k][submatrix_j+n] == value:
                return False

    return True

def sudoku(arr, x, y):
    if x == len(arr) or y == len(arr[0]):
        for i in range(len(arr)):
            print(arr[i], end=" ")
            print(sep="\n")
        return

    next_i = 0
    next_j = 0

    if y == len(arr[0])-1:
        next_i = x + 1
        next_j = 0
    else:
        next_i = x
        next_j = y  + 1   

    if arr[x][y]:
        sudoku(arr, next_i, next_j)
    else:
        for i in range(1, 10):
            if isvalid(arr, x, y, i):
                arr[x][y] = i
                sudoku(arr, next_i, next_j)
                arr[x][y] = 0


matrix = [
    [3, 0, 6, 5, 7, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]
sudoku(matrix, 0, 0)