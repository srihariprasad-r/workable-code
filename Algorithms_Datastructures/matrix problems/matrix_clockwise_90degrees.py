"""

Input : 

[[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]]

Output:

[[13,9,5,1],
[14,10,6,2],
[15,11,7,3],
[16,12,8,4]]
"""

def rotatematrix(matrix):
    n = len(matrix)
    for i in range(n):        
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    
    for i in range(n):
        for j in range(0, int(n/2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-j-1]
            matrix[i][n-j-1] = temp
    
    for i in range(n):
        print(matrix[i])

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rotatematrix(matrix)