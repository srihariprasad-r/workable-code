def tile_problem(n):
    tile = [0] * (n+1)
    tile[1] =  1
    tile[2] =  2

    for i in range(3, n+1):
        tile[i] = tile[i-1] + tile[i-2]
    
    print(tile[-1])

tile_problem(5)