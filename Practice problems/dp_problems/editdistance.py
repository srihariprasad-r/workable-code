def editdistance(s1, s2, m, n):
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                if s2[j-1] == s1[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                    
    return dp[m][n]
                
s1 = "sunday"
s2 = "saturday"
m = len(s1)
n = len(s2)
print(editdistance(s1, s2, m, n))