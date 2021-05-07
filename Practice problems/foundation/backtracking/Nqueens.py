"""
Queens attack other queen diagonally, vertically.
So we build diagnoal and reverse diagnal matrix to check which will be valid position for Queen to survive

1. cols list is to store columns visited
2. ndiag list will store row + col as index and set to True when visited
3. revdiag list will store r-c + len(board) + 1 and set to True when visited

So we will assign Queen to be valid position, if there is no other diagnoal crossing the same vertex

If so, we backtrack this and do for all rows.
"""
def Nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    cols = [False] * (n)
    diagonals = [False] * (2 * n - 1)
    reversediagonals = [False] * (2 * n- 1)
    solve(board, 0, cols, diagonals, reversediagonals)


def solve(brd, r, col, nd, rd, ans=[]):
    if r == len(col):
        print(ans)
        return 

    for j in range(len(brd[0])): 
        if not brd[r][j] and not col[j] and not nd[r+j] and not rd[r-j+len(brd)-1]:
            brd[r][j] = 1
            col[j] = True
            nd[r+j] = True
            rd[r-j+len(brd)-1] = True
            solve(brd, r+1, col, nd, rd, ans + [str(r) + " -> " + str(j)])
            brd[r][j] = 0
            col[j] = False
            nd[r+j] = False
            rd[r-j+len(brd)-1] = False

n = 4
print(Nqueens(4))