"""
k = 2 #number of times matrix to be rotated

Input : 

[[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]]

Output:

[[4,3,1,2],
[8,7,5,6],
[12,11,9,10],
[16,15,13,14]]
"""

def rotatematrix(matrix,k):
    n = len(matrix)
    k = k%n #rounding off to nearest reminder if k >> m

    temp = [0] * n

    for i in range(0, n):
        for t in range(0, n-k):
            temp[t] = matrix[i][t]
        
        for j in range(n-k, n):
            matrix[i][j-n+k] = matrix[i][j]
        
        for j in range(k, n):
            matrix[i][j]= temp[j-k]
    
    for i in range(n):
        print(matrix[i])



matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rotatematrix(matrix, k = 2)