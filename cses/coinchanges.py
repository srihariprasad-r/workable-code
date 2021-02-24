def coinchanges(n, coins):
    dp = [0 for i in range(n+1)]
    
    dp[0] = 1
    
    for i in range(1, n+1):
        for j in range(0, len(coins)):
            if coins[j] > i:
                continue
            else:
                dp[i] = dp[i] + dp[i-coins[j]]
                
    print(dp)

n = 5
coins = [2, 3, 5]
print(coinchanges(n, coins))