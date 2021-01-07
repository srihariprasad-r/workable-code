def subseq_sum_less_than_k(arr, k):  
  n = len(arr)

  dp = [[0 for i in range(k)] for j in range(n)]

  for i in range(n):
    if arr[i]  < k:
      dp[i][0] = 1

    for j in range(k):
        if arr[0] <= k - 1:
            dp[0][j] = 1
 
    for i in range(1,n):
        for j in range(1,k):
            excludes = 0
            includes = 0            
            if arr[i] <= k -1:
                includes = dp[i-1][k - arr[i]]            
            excludes = dp[i-1][k-1]
                    
            dp[i][j] = includes + excludes

    print(dp)

arr = [25, 13, 40]
k = 50
print(subseq_sum_less_than_k(arr, k))