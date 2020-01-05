mat = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
]

def matrix_transpose(n,mat):
    for i in range(n): 
        j = 0
        k = n-1
        while j < k: 
            print(i,j,k)
            t = mat[j][i] 
            mat[j][i] = mat[k][i] 
            mat[k][i] = t 
            j += 1
            k -= 1    
        print(mat)


matrix_transpose(4,mat)