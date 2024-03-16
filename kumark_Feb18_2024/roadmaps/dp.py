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

# question link: https://www.desiqna.in/13822/google-dp-interview-question-jan-2023
# arr = [5, 4, 2, 6]
arr = [2 ,3 ,5, 8, 10]

dp = [0] * len(arr)

def oddsum(idx, s):
    if idx < 0:
        return 0
    
    if idx == 0:
        s += arr[idx]
        if s % 2 == 0: return 1
        else: return 0
    
    # commented as it provides incorrect results
    # if dp[idx] != 0: return dp[idx]
    
    odd_s_1 = 0
    odd_s_2 = 0
    
    odd_s_1 = oddsum(idx-1, s + arr[idx])
    odd_s_2 = oddsum(idx-2, s + arr[idx])
    
    dp[idx] = odd_s_1 + odd_s_2
    return dp[idx]

print(oddsum(len(arr)-1, 0))