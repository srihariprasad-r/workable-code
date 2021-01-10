def unboundedknapsack(wt, val, w):
    dp = [[0 for x in range(w+1)] for y in range(len(wt))]

    for i in range(0,len(wt)):
        for j in range(1,w+1):
            incl = 0
            if wt[i] <= j:
                incl = val[i] + dp[i][j-wt[i]]
            dp[i][j] = max(incl , dp[i-1][j])
            
    return dp[-1][-1]


wt = [1, 2, 3, 5]
val = [1, 4, 7, 10]
w = 8
print(unboundedknapsack(wt, val, w))