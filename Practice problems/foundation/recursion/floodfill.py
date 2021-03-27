def floodfill(maze, psf, n, m, visited):
    if n < 0 or m < 0 or n == len(maze) or m == len(maze[0]) or maze[n][m] == 1 or visited[n][m]:
        return
    
    if n == len(maze)-1 and m == len(maze[0])- 1:
        print(psf)
        return

    visited[n][m] = True
    floodfill(maze, psf + "t", n, m, visited)
    floodfill(maze, psf + "l", n, m - 1, visited)
    floodfill(maze, psf + "d", n + 1, m, visited)
    floodfill(maze, psf + "r", n, m + 1 , visited)
    visited[n][m] = False       # this flag will reset visited points for next route check

maze = [
    [0, 1, 1],
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0]
]
psf = ""
visited = [[False for i in range(len(maze[0]))] for j in range(len(maze))]
floodfill(maze, psf, 0, 0, visited)
