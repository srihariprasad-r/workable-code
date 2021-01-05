def knapsack(wt, val, w):
    dp = [[0 for x in range(w+1)] for y in range(len(wt))]

    tmp = dp[0]

    for i in range(len(dp[0])): 
        if i >= wt[0]:
            tmp[i] = val[0]

    for i in range(1,len(wt)):
        for j in range(1,w+1):
            incl = 0
            if wt[i] <= j:
                incl = val[i] + dp[i-1][j-wt[i]]
            dp[i][j] = max(incl , dp[i-1][j])

    return dp[-1][-1]


wt = [1, 2, 3, 5]
val = [1, 4, 7, 10]
w = 8
print(knapsack(wt, val, w))