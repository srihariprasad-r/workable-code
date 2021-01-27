"""
To find mimimum cost path, we create dp array and below will be logic
1. Last row and last column will have same value as array as it is source
2. Last row is filled with horizontal moves only as there will not be any option to move vertical(downwards) as arrays ends
3. Last column is filled with only vertical direction values as horizontal direction will not be available
4. For other values, we take minimum(right element, down element) to current element from dp array and add it with array value
"""

def mincostpath(arr, n, m):
    dp = [[0 for i in range(n)] for j in range(m)]

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i == len(arr)-1 and j == len(arr) - 1:
                dp[i][j] = arr[i][j]
            elif i == len(arr) - 1:
                dp[i][j] = dp[i][j+1] + arr[i][j]
            elif j == len(arr) - 1:
                dp[i][j] = dp[i+1][j] + arr[i][j]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + arr[i][j]

    return dp


arr = [
    [2, 8, 4, 1, 6, 4, 2],
    [6, 0, 9, 5, 3, 8, 5],
    [1, 4, 3, 4, 0, 6, 5],
    [6, 4, 7, 2, 4, 6, 1],
    [1, 0, 3, 7, 1, 2, 7],
    [1, 5, 3, 2, 3, 0, 9],
    [2, 2, 5, 1, 9, 8, 2]
]
n = 7
m = 7
print(mincostpath(arr, n, m))