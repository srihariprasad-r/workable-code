def distincttransformation(s, t):
    dp = [[-1 for i in range(len(s))] for j in range(len(t))]

    for i in range(len(t)-1, -1, -1):
        for j in range(len(s)-1, -1, -1):
            if i == len(dp) - 1:
                dp[i][j] = 1
            elif j == len(dp[0]) -1 :
                dp[i][j] = 0
            else:
                if s[j] == t[i]:
                    dp[i][j] = dp[i][j+1] + dp[i+1][j+1]
                else:
                    dp[i][j] = dp[i][j+1]


    return dp[0][0]


s = 'aaabbc'
t = 'abc'
print(distincttransformation(s, t))