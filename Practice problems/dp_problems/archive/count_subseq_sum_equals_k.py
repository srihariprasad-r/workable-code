def subseq_sum_equals_k(arr, k):
    count = 0

    dp = [[0 for i in range(k+1)] for j in range(len(arr))]

    for i in range(len(arr)):        
        dp[i][0] = 1

    for j in range(k+1):
        if arr[0] == j:
            dp[0][j] = 1
 
    for i in range(1,len(arr)):
        for j in range(1,k+1):
            excludes = 0
            includes = 0            
            if arr[i] <= j:
                includes = dp[i-1][j-arr[i]]            
            excludes = dp[i-1][j]
                    
            dp[i][j] = includes + excludes

    return dp[-1][-1]

arr = [2,3,7,1,4,5]
print(subseq_sum_equals_k(arr, 7))