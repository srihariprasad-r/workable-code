def countsubsetsum(arr, csum):
    dp = [[0 for i in range(csum+1)] for j in range(len(arr) + 1)]

    for j in range(len(arr)+1):
        dp[j][0] = 1

    for i in range(1,len(arr)+1):
        for j in range(1, csum+1):
            if j >= arr[i-1]:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]

arr = [2, 3, 5, 8, 10]
tsum = 10
print(countsubsetsum(arr, tsum))