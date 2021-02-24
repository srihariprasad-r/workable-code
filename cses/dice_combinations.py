def dicecombinations(n):
    dp = [0 for i in range(n+1)]
    
    dp[0], dp[1]= 1, 1
    
    for i in range(2, n+1):
        for j in range(1, 7):
            if j > i:
                continue
            else:
                dp[i] = dp[i] + dp[i-j]
                
    print(dp)

n = 3
print(dicecombinations(n))