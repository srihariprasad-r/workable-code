def longest_increasing_subsequence(arr):
  n = len(arr)
  dp = [1 for i in range(n)]

  for i in range(1, n):
    for j in range(0, i):
      if arr[i] > arr[j] and dp[i] < dp[j] + 1:
        dp[i] = dp[j] + 1
         
  return max(dp)

arr = [7, 1, 4, 8, 11, 2, 14, 3]
print(longest_increasing_subsequence(arr))