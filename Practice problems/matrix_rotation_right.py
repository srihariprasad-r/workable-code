mat = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
]

def matrix_rotation(n,mat):
    for i in range(0, n/2):
        for j in range(i, n-i-1):
            temp = mat[i][j]
            mat[i][j] = mat[j][n-i-1]
            mat[j][n-1-i] = mat[n-i-1][n-j-1]
            mat[n-i-1][n-j-1] = mat[n-j-1][i]
            mat[n-j-1][i] = temp
    print(mat)


matrix_rotation(4,mat)


