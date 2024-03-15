# question link: https://docs.google.com/document/d/13ydHMmLXcvIbpvH-rn-9F3Oc4IiekKu8ItLr05HZRJI/edit
# wrong submission
n = 15

y = 100
x = 1 
z = 50
b = 100000

m = n
dp = [0] * 16

def min_cost(dp, m):
    n = 1

    while  n <= m:
        dp[n // 1] += y
    
        if n % 7 == 0:
            dp[n//7] += x
            
        if n % 3 == 0:
            dp[n//3] += z
    
        if n % 5 == 0:
            dp[n//5] += b
            
        dp[m] = min(dp[n//1], min(dp[n//7], min(dp[n//3], dp[n//5])))
        
        n += 1
    
    return dp[m]  
    
print(min_cost(dp, m))