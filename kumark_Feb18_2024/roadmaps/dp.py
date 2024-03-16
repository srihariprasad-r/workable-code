# question link: https://docs.google.com/document/d/13ydHMmLXcvIbpvH-rn-9F3Oc4IiekKu8ItLr05HZRJI/edit
# wrong submission
n = 15

y = 100
x = 1 # /7 
z = 50 # /3
b = 100000 # /5

m = n
dp = [0] * 16
dp[1] = y

def min_cost(dp, m):
    n = 2
    while n <= m:

        e1 = 100000001
        e2 = 100000001
        e3 = 100000001
        
        dp[n // 1] += y

        if n % 7 == 0:
            e1 = dp[n//7] + x
            
        if n % 3 == 0:
            e2 = dp[n//3] + z
    
        if n % 5 == 0:
            e3 = dp[n//5] + b

        v = min(dp[n//1], min(e1, min(e2, e3)))

        dp[n] = v
        n += 1

    return dp[m] 
    
print(min_cost(dp, m))