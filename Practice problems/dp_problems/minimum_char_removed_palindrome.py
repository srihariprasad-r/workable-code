def longest_palindrome_substring(str1):
    n = len(str1)
    str2 = str1[::-1]

    dp = [[0 for i in range(n+1)] for j in range(n+1)]

    for i in range(1,n+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    print(n - dp[n][n])

str1 = "ACBCDBAA"
longest_palindrome_substring(str1)