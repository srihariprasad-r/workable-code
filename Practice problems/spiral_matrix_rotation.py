a = [ [1, 2, 3], 
      [7, 8, 9], 
      [13, 14, 15] 
    ]

#m == number of columns
#n == number of rows

m = 3
n = 3

def spiral_matrix(a):
    top = 0
    right = m - 1
    bottom = n - 1
    left = 0
    while (top <= bottom and left <= right):
        for i in range(left, right+1):
            print(a[top][i])
        top = top + 1
        for i in range(top, bottom+1):
            print(a[i][right])
        right = right - 1
        for i in range(right, left-1,-1):
            print(a[bottom][i])
        bottom = bottom -1
        for i in range(bottom,top-1,-1):
            print(a[i][left])
        left = left + 1

spiral_matrix(a)