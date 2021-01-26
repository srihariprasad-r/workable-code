def maxsumincreasingsubsequence(arr):
    smax = 0
    dp = [-1] * len(arr)

    dp[0] = arr[0]

    for i in range(1, len(arr)):
        mx, j = 0, 0
        while j < i:
            if arr[j] < arr[i]:
                if dp[j] > mx:
                    mx = dp[j]
            j += 1
        dp[i] = mx + arr[i]

        if dp[i] > smax:
            smax = dp[i]

    return smax


arr = [10, 22, 9, 33, 21, 50, 41, 60, 80, 9]
print(maxsumincreasingsubsequence(arr))