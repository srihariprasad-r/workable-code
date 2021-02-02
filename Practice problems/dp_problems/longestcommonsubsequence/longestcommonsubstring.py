def longestcommonsubstring(s1, s2):
    mx = 0
    dp = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

    for i in range(1,len(s2)):
        for j in range(1,len(s1)):
            if s2[i] == s1[j]:
                dp[i][j] = dp[i-1][j-1] + 1
                if mx < dp[i][j]:
                    mx = dp[i][j]
            else:
                dp[i][j] = 0 

    return mx

s1 = 'pqabcxy'
s2 = 'xyzabcp'
print(longestcommonsubstring(s1, s2))