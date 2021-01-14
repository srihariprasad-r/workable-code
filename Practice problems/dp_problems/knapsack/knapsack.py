"""
Notes:
1.X-axis will be capacity, Y-axis will represent weights
2.If capacity is 0, profit gained will be zero, so all first column will be defaulted to 0
3.For first row, we assign lowest weight for columns which have capacity >= lowest weight
4. For remaning rows,
    a. We exclude current weight in case capacity < current weight.
        Take previous row value
    b. We include current weight in case capcacity >= current weight
        Take current weight profit + previous row's profit of capacity remains ( current weight - capacity)
5. Take maximum(excluding current weight + including current weight)
"""
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