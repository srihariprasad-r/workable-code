"""
split n members into k teams

1. When n = 0 or k = 0 , dp[i][j] = 1
2. when k = 1, there is only one team for all memebers, so dp[i][j] = 1
3. when n < k, dp[i][j] = 0
4. when n > k => k*f(n-1(k)) + f(n-1)(k-1)
"""

def partitionsubsets(n,k):
    dp = [[0 for i in range(n+1)] for j in range(k+1)]
    
    for i in range(k+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0    # when either n = 0 or k = 0
            elif i == 1:
                dp[i][j] = 1    # when k =1, there is only one team
            elif i == j:
                dp[i][j] = 1    # when n == k
            else:
                dp[i][j] = i * dp[i][j-1] + dp[i-1][j-1]
                
    return dp[-1][-1]
    
n = 4 # members
k = 3 # teams
print(partitionsubsets(n,k))