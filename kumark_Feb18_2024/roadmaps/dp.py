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

# question link: https://www.desiqna.in/16115/google-interview-problem-dynamic-programming-cities-october#google_vignette
# A = [23, 4,5 ,101] 
# B = [21,1,10, 100]

A = [25,10,15,10,70] 
B = [5,5,50,5,30]

dp = [0] * len(A)

dp[0] = max(A[0], B[0])

def travel_city(A,B, dp):
    placework = 'A' if A[0] > B[0] else 'B'
    for i in range(1, len(A)):
        if placework == 'A':
            if dp[i-1] + A[i] > dp[i-2] + B[i]:
                dp[i] = A[i] + dp[i-1]
            else:
                dp[i-1] = dp[i-2]
                dp[i] = dp[i-2] + B[i]
                placework = 'B'
        else:
            if dp[i-2] +A[i] > dp[i-1] + B[i]:
                placework = 'A'
                dp[i-1] = dp[i-2]
                dp[i] = dp[i-2] + A[i]
            else:
                dp[i] = B[i] + dp[i-1]
                
    return dp[-1]
                
print(travel_city(A, B, dp))