"""
Find exit point in matrix.

We consider four directions, N, W, E, S. 
E -> 0 (moves right)
S -> 1 (moves down)
W -> 2 (moves left)
N -> 3 (move top)

If we reach any border in row/column, we print that co-ordinate
"""
def exitpointmatrix(arr):
    n, m = len(arr), len(arr[0])
    direction = 0
    i , j = 0, 0
    
    while True:
        direction = (direction + arr[i][j])% 4 # modulo is applied to rotate between 0 and 3
        
        if direction == 0:
            j += 1
        elif direction == 1:
            i += 1
        elif direction == 2:
            j -= 1
        elif direction == 3:
            i -= 1
        
        if i < 0:
            i += 1
            break
        elif j < 0:
            j += 1
            break
        elif i == len(arr):
            i -= 1
            break
        elif j == len(arr[0]):
            j -=1 
            break
        
    print(i, j)
        

arr = [
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [1, 0, 1, 0]
]

print(exitpointmatrix(arr))