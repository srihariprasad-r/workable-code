def countpalindromesubstring(str1):
    cnt = 0
    dp = [[False for i in range(len(str1))] for j in range(len(str1))]

    for g in range(len(str1)):
        j = g
        for i in range(len(str1)):
            if g == 0:              # across diagonal. g represents gap, gaps starts in first row and ends in last column
                dp[i][j] = True     # all strings have single character, they match and create palindorme
            elif g == 1:            
                if str1[i] == str1[j]:
                    dp[i][j] = True     # here values will be 'aa', 'bb', so they are made true when first and last char match
            elif str1[i] == str1[j] and dp[i+1][j-1]:
                """
                We match first and last character match, if that is true, we take next row and previous column to check if its valid
                For example: bccb , first and last character match, so we proceed checking if cc is palindrome, update that row in dp
                """
                dp[i][j] = True


            if dp[i][j]:
                cnt += 1

            if j < len(str1)-1:
                j += 1 
            else:
                break

    return cnt

str1 = 'abcd'
print(countpalindromesubstring(str1))