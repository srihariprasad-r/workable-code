def repeatingsubsequence(s):
    a = s
    b = s
    rep_str = set()
    dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
    
    for i in range(1,len(s)+1):
        for j in range(1, len(s)+1):
            if a[i-1] == b[j-1] and i != j:
                dp[i][j] = dp[i-1][j-1] + 1
                rep_str.add(b[j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return ''.join(list(map(lambda x: str(x), rep_str))) if rep_str else False
    
s =  'XYZABCX'
print(repeatingsubsequence(s))