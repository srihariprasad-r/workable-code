def count_subsequence_pattern_k_times(s, ptn, k):
    new_pttrn = s * k
    cnt = 0
    
    dp = [[0 for _ in range(len(ptn)+1)] for _ in range(len(new_pttrn) + 1)]
    
    for i in range(1, len(new_pttrn)+1):
        for j in range(1, len(ptn)+1):
            if new_pttrn[i-1] == ptn[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                cnt += 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                
    return  cnt
    
s = 'subsequence'
ptn = 'sue'
k = 1
print(count_subsequence_pattern_k_times(s, ptn, k))