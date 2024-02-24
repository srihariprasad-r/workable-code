# max sum non adjacent

arr = [2,-3,5,-8,7]

dp = [0] * len(arr)
dp[0] = arr[0]
dp[1] = max(dp[0], arr[1])

def maxsum_nonadj(arr):
    for i in range(2, len(arr)):
        dp[i] = max(dp[i-2]+arr[i], dp[i-1])
        
    return max(dp)
    
print(maxsum_nonadj(arr))

# maximum sum subsets for both arrays - not adjacent
a = [2,3,4,-8,2]
b = [-5,8,3,1,-4]

dp = [0] * len(a)
dp[0] = max(a[0],b[0])
dp[1] = max(dp[0], max(a[1],b[1]))

def maxsum_nonadj(arr1,arr2):
    for i in range(2, len(arr1)):
        dp[i] = max(dp[i-2]+max(arr1[i],arr2[i]), dp[i-1])
        
    return max(dp)
    
print(maxsum_nonadj(a,b))

# frog jump 1

arr = [10, 30, 40,20]

dp = [float('inf')] * len(arr)
dp[0] = 0
dp[1] = abs(arr[1]-arr[0])

def maxsum_nonadj(arr):
    for i in range(2, len(arr)):
        dp[i] = min(dp[i-1]+abs(arr[i]-arr[i-1]), dp[i-2]+abs(arr[i]-arr[i-2]))

    return dp[-1]
    
print(maxsum_nonadj(arr))

# frog k jumos

arr = [40, 10, 20, 70, 80, 10, 20, 70, 80, 60]
k = 4

dp = [float('inf')] * len(arr)
dp[0] = 0
dp[1] = abs(arr[1]-arr[0])

def maxsum_nonadj(arr,k):
    for i in range(2, len(arr)):
        for j in range(1, k+1):
            dp[i] = min(dp[i-j]+abs(arr[i]-arr[i-j]), dp[i])

    return dp[-1]
    
print(maxsum_nonadj(arr,k))