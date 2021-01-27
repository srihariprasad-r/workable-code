"""
To find subsequences of non empty string, we do as below:
1. First element is treated with blank, so dp array is initialized with len(s)+1
2. we run loop from 1 to len(s), 
    dp = [0 1 2 3 4 5 6 7...]
            ^ ^ ^ ^ ^ ^ ^
            | | | | | | |         
            0 1 2 3 4 5 6   <- string index
3. when each character is new, we add it to dp array with dp index
4. If its not there, we update current dp index with 2 * dp[i-1]
5. If its repeating, we account for previously occured distinct subsequence and remove that count
    So, we do dp[i] = dp[i] - dp[dct[s[i-1]]] 
"""
def countdistinctsubsequence(s):
    dct = {}
    dp = [0] * (len(s) + 1)
    dp[0] = 1   # initial assignment for blank which is considered with 1 subsequence

    for i in range(1, len(s)+1):
        dp[i] = 2 * dp[i-1]
        if s[i-1] not in dct:
            dct[s[i-1]] = i
        else:
            j = dct[s[i-1]]
            dp[i] = dp[i] - dp[j - 1]

    return dp[len(s)]-1    
    


s = 'abcbac'
print(countdistinctsubsequence(s))