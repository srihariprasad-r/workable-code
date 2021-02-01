def largestsquaresubmatrixall1s(arr):
    n = len(arr)
    m = len(arr[0])
    dp = [[0 for i in range(m)] for j in range(n)]
    mn, mx = 0, 0

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if arr[i][j] == 0:
                dp[i][j] = 0
            else:
                if i == n-1 and arr[i][j] != 0:
                    dp[i][j] = 1
                elif j == m-1 and arr[i][j] != 0:
                    dp[i][j] = 1
                else:
                    mn = min(dp[i][j+1], dp[i+1][j])
                    dp[i][j] = min(mn, dp[i+1][j+1]) + 1
                    # update mx if dp[i][j] exceeds
                    mx = max(mx, dp[i][j])

    return mx

arr = [
    [0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1]
]
print(largestsquaresubmatrixall1s(arr))