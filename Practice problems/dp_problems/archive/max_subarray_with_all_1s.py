def max_subarray_matrix(M):
    rows = len(M)
    cols = len(M[0])

    new_matrix = [[0 for i in range(cols)] for k in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            if M[i][j] == 1:
                new_matrix[i][j] = 1 + min(new_matrix[i-1][j], new_matrix[i][j-1], new_matrix[i-1][j-1])
            else:
                new_matrix[i][j] = 0
    
    maxval_new_matrix = 0
    max_row_val = 0
    max_val_col = 0

    for i in range(len(new_matrix)):
        for j in range(i):
            if maxval_new_matrix < new_matrix[i][j]:
                maxval_new_matrix = new_matrix[i][j]
                max_row_val = i 
                max_val_col = j

    
    for i in range(max_row_val, max_row_val - maxval_new_matrix , -1):
        for j in range(max_val_col, max_val_col - maxval_new_matrix , -1):
            print(M[i][j], end=" ")
        print(" ")

M = [[0, 1, 1, 0, 1], 
    [1, 1, 0, 1, 0], 
    [0, 1, 1, 1, 0], 
    [1, 1, 1, 1, 0], 
    [1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0]] 

max_subarray_matrix(M)