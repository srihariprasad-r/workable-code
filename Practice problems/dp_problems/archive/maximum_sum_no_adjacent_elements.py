def maximum_sum_no_adjacent_elements(arr):
  n = len(arr)
  dp = [0 for i in range(n)]

  dp[0] = arr[0]
  dp[1] = max(dp[0], arr[1])

  for i in range(2, n):
    dp[i] = max(arr[i] + dp[i-2], dp[i-1])

  return dp[-1]

arr = [4,2,3,5,1,6,7]
print(maximum_sum_no_adjacent_elements(arr))