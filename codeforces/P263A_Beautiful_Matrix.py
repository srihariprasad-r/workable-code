matrix = []
n = 5

while n > 0:
    matrix.append([int(x) for x in input().split(" ")])
    n -= 1

row_i = 0
row_j = 0
mid_row = 3
mid_col = 3

for i in range(len(matrix)):    
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            row_i = i + 1
            row_j = j + 1

dist = abs(mid_row - row_i) + abs(mid_col - row_j)
print(dist)
