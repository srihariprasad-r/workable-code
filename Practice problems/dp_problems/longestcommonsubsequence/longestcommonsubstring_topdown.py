def lcs_topdown(str1, str2, n, m):
    mx= 0
    if n == 0 or m == 0:
        return mx

    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i == 0 or j == 0:
                dp[i][j] = 0

    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                mx = max(dp[i][j], mx)
            else:
                dp[i][j] = 0

    return mx


str1 = 'abcde'
str2 = 'abfce'
dp = [[-1 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
print(lcs_topdown(str1, str2, len(str1), len(str2)))