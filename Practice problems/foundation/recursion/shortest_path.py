def shortestpath(mat, st, end, dest_x, dest_y, ans=[], res=[]):
    if st > dest_x or end > dest_y:
        return

    if st == dest_x and end == dest_y:
        res.append(ans)
        return

    if mat[st+1][end]:
        shortestpath(mat, st+1, end, dest_x, dest_y, ans + [(st, end)], res)

    if mat[st][end+1]:
        shortestpath(mat, st, end+1, dest_x, dest_y, ans + [(st, end)], res)

    return res


mat = [
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]
src = (0, 0)
dest = (7, 5)
print(shortestpath(mat, src[0], src[1], dest[0], dest[1]))
