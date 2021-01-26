def countpalindromesubstring(str1):
    cnt = 0
    dp = [[False for i in range(len(str1))] for j in range(len(str1))]

    for g in range(len(str1)):
        j = g
        for i in range(len(str1)):
            if g == 0:
                dp[i][j] = True
            elif g == 1:
                if str1[i] == str1[j]:
                    dp[i][j] = True
            elif str1[i] == str1[j] and dp[i+1][j-1]:
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