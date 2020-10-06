def longest_increasing_subsequence_adjacent_diff_is_one(arr):
  n = len(arr)
  dp = [1 for i in range(n)]

  for i in range(1, n):
    for j in range(0, i):
      if (arr[i] > arr[j] - 1 or arr[i] == arr[j] - 1) and dp[i] < dp[j] + 1:
        dp[i] = dp[j] + 1
         
  return max(dp)

arr = [1, 2, 3, 4, 5, 3, 2]
print(longest_increasing_subsequence_adjacent_diff_is_one(arr))