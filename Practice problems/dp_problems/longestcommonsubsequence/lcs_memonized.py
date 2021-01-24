def lcs_memonized(x, y, n, m):
    if n== 0 or m == 0:
        return 0

    if dp[m][n] != -1:
        return dp[m][n]

    if x[n-1] == y[m-1]:
        dp[m][n] =  1 + lcs_memonized(x, y, n-1, m-1)
    else:
        dp[m][n] =  max(lcs_memonized(x, y, n, m-1), lcs_memonized(x, y, n-1, m))

    return dp[m][n]

x = 'abcdegh'
y = 'abcdfr'
dp = [[-1 for i in range(len(x)+1)] for j in range(len(y)+1)]
print(lcs_memonized(x,y, len(x), len(y)))