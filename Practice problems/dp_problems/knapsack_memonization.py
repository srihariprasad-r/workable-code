def knapsack_memonization(dp, wt, val, w, n):
    if (n == 0 or w == 0):
        return 0

    if dp[n][w] != -1:
        return dp[n][w]

    if w >= wt[n-1]:
        dp[n][w] =  max(val[n-1] + knapsack_memonization(dp, wt, val, w- wt[n-1], n-1),
                    knapsack_memonization(dp, wt, val, w, n-1))
    
    if w < wt[n-1]:
        dp[n][w] = knapsack_memonization(dp, wt, val, w, n-1)

    return dp[n][w]


wt = [1, 2, 3, 5]
val = [1, 4, 7, 10]
w = 8
n = len(wt)
dp  = [[-1 for x in range(w + 1)] for y in range(n+1)]
print(knapsack_memonization(dp, wt, val, w, n))