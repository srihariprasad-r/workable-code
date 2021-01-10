def subset_equal_sum(trgt_sum, subset):
    dp = [[False for x in range(trgt_sum + 1)] for y in range(len(subset))]

    for i in range(len(subset)):
        dp[i][0] = True

    for j in range(trgt_sum+1):
        if subset[0] == j:
            dp[0][j] = True

    for i in range(1, len(subset)):
        for j in range(1,trgt_sum+1):
            if dp[i-1][j]:
                dp[i][j] = True
            elif j >= subset[i]:    #if value is greater than subset item, then include
                dp[i][j] = dp[i-1][j-subset[i]]     #0/1 knapsack
    
    return dp[-1][-1]

subset = [1,2, 3, 5]
trgt_sum = 7
print(subset_equal_sum(trgt_sum, subset))
