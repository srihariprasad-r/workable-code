def mazepath(src_row, src_col, dest_row,dest_col):
    if src_col == dest_col and src_row == dest_row:
        return [""]

    hpaths, vpaths = [], []
    
    if src_row < dest_row:
        hpaths = mazepath(src_row+1, src_col, dest_row, dest_col)

    if src_col < dest_col:
        vpaths = mazepath(src_row, src_col + 1, dest_row, dest_col)

    paths = []
    for h in hpaths:
        paths.append('h' + h)
    
    for v in vpaths:
        paths.append('v' + v)
    
    return paths

print(mazepath(1, 1, 3, 3))