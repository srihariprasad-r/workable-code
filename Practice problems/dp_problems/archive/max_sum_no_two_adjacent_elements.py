def maximum_sum_no_two_adjacent_elements(arr):
  n = len(arr)
  dp = [0 for i in range(n)]

  dp[0] = arr[0]
  dp[1] = arr[0] + arr[1]
  dp[2] = max(arr[2], dp[1])

  for i in range(3, n):
    dp[i] = max(arr[i] + dp[i-3], dp[i-2])

  return dp[-1]

arr = [3000, 2000, 1000, 3, 10]
print(maximum_sum_no_two_adjacent_elements(arr))