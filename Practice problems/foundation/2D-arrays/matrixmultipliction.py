"""
To mutiply two matrices, column of first matrix should match to row of second matrix

A= [
a11 a12 a13
a21 a22 a23
]

B= [
b11 b12 b13
b21 b22 b23
b31 b32 b33
]

AxB = [
a11.b11+a12.b21+a13.b31 .....
.....   ......
]

If we notice for first matrix column changes, and for second matrix row changes, we include k which is either c1/r2 and do as below
a[i][k] * b[k][j] where i runs till r1; j till c2; k runs till c1/r2

"""

def matrixmultiply(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])

    if c1 != r2:
        return
    
    prd = [[0 for i in range(c2)] for j in range(r1)]

    for i in range(len(prd)):
        for j in range(len(prd[0])):
            for k in range(c1):
                prd[i][j] += arr1[i][k]*arr2[k][j]
                
    
    return prd
        


arr1 = [
    [1, 2, 3],
    [4, 5, 6]
]

arr2 = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6]
]

print(matrixmultiply(arr1, arr2))