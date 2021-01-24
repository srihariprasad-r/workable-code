def lcs_topdown(x, y, n, m):
    for i in range(len(x)+1):
        for j in range(len(y)+1):
            if i == 0 or j == 0:
                dp[i][j] = 0

    for i in range(1,len(x)+1):
        for j in range(1, len(y)+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]

x = 'abcd'
y = 'abcdef'
dp = [[-1 for i in range(len(y)+1)] for j in range(len(x)+1)]
print(lcs_topdown(x, y, len(x), len(y)))