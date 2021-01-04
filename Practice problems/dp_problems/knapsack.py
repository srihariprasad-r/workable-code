def knapsack(wt, val, w):
    dp = [[0] * (w + 1)] * len(wt)

    for i in range(w+1):
        if wt[0] <= i:
            dp[0][i] = wt[0]

    for i in range(w+1):
        for j in range(len(wt)+1):
            if wt[j] <= i:
                incl = val[i] + dp[i-1][i-wt[j]]
        dp[i][j] = incl + dp[i-1][j]

    print(dp)


wt = [1, 2, 3, 5]
val = [1, 4, 7, 10]
w = 8
print(knapsack(wt, val, w))