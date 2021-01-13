"""
Here the logic is to find if target sum arrived after sum of elements in the array leads
to odd, if its odd, there is no way for equal partition sum subset

In case it is negative, we will use subset sum logic and send target sum as totalsum of array // 2 
This is done if in that array we have sum of totalsum of array // 2, this shows that equal subset sum exists
as other subset will have the totalsum of array // 2 since the total sum is even

"""

def equal_sum_partition(arr):
    sum_t = 0
    for i in range(len(arr)):
        sum_t += arr[i]

    if sum_t % 2 != 0:
        return False
    else:
        return subsetsum(arr, sum_t//2)

def subsetsum(arr, tsum):
    dp = [[False for i in range(tsum+1)] for y in range(len(arr)+1)]

    for i in range(len(dp)):
        for j in range(tsum+1):
            if j == 0:
                dp[i][j] = True

    for i in range(1,len(dp)):
        for j in range(1,tsum+1):
            dp[i][j] = dp[i-1][tsum - j] or  dp[i-1][tsum]

    return dp[-1][-1] 


arr = [1, 5, 5, 11]
tsum = 11
print(equal_sum_partition(arr))
