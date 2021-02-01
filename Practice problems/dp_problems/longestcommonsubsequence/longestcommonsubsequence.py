def longestcommonsubsequence(s1, s2):
    dp = [[-1 for i in range(len(s1)+1)] for j in range(len(s2)+1)]

    for i in range(len(s2),-1, -1):
        for j in range(len(s1), -1, -1):
            if i == len(s2):
                dp[i][j] = 0
            elif j == len(s1):
                dp[i][j] = 0
            else:
                if s1[j] == s2[i]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

    return dp[0][0]               

s1 = 'abcd'
s2 = 'abed'
print(longestcommonsubsequence(s1, s2))