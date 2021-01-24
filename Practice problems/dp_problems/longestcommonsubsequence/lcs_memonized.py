def lcs_memonized(x, y, n, m):
    if n== 0 or m == 0:
        return 0

    if dp[n-1][m-1] != -1:
        return dp[n-1][m-1]

    if x[n-1] == y[m-1]:
        dp[n-1][m-1] =  1 + lcs_memonized(x, y, n-1, m-1)
    else:
        dp[n-1][m-1] =  max(lcs_memonized(x, y, n, m-1), lcs_memonized(x, y, n-1, m))

    return dp[n-1][m-1]

x = 'abcdegh'
y = 'abcdfr'
dp = [[-1 for i in range(len(y))] for j in range(len(x))]
print(lcs_memonized(x,y, len(x), len(y)))