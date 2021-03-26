def mazepath_jumps(src_row, src_col, dest_row,dest_col):
    if src_col == dest_col and src_row == dest_row:
        return [""]

    paths = []
    
    i = 1 
    while i <= dest_col - src_col:
        hpaths = mazepath_jumps(src_row , src_col + i, dest_row, dest_col )
        for h in hpaths:
            paths.append('h' + str(i)  + h)
        i += 1

    j = 1 
    while j <= dest_row - src_row:
        vpaths = mazepath_jumps(src_row + j , src_col, dest_row, dest_col )
        for v in vpaths:
            paths.append('v' + str(j)  + v)
        j += 1

    k = 1 
    while k <= dest_row - src_row and k <= dest_col - src_col:
        dpaths = mazepath_jumps(src_row + k , src_col+ k, dest_row, dest_col )
        for d in dpaths:
            paths.append('d' + str(k)  + d)
        k += 1

    return paths

print(mazepath_jumps(1, 1, 3, 3))