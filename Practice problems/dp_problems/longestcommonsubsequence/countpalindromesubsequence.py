def countpalindromesubsequence(str):
    dp = [[0 for i in range(len(str))] for j in range(len(str))]

    for g in range(len(str)):
        j = g
        for i in range(len(str)):
            if g == 0:
                dp[i][j] = 1
            elif g == 1:
                if str[i] == str[j]:
                    """
                    when length of substring is 2 such as 'ab', palindrome subsequences are a & b.
                    so when str = 'cc', palindrome subsequences are c, c && c which are 3 in count
                    """
                    dp[i][j] = 3
                else:
                    dp[i][j] = 2
            else: 
                if str[i] == str[j]:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1
                    """
                    when first and last characters match, we do the following:
                       str = 'acbca' -> c1= 1; m = cbc; c2 = a
                       c1 == c2, so prefix = 'acbc'; suffix = 'cbca'; m = 'cbc'
                       c(prefix) + c(suffix) + 1
                       prefix is same row and previous column
                       suffix is next row same column
                       m is previous row and previous column
                    """
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]  

            if j < len(str) -1 :
                j += 1
            else:
                break

    return dp[0][-1]

str = 'abccbc'
print(countpalindromesubsequence(str))