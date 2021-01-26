def lis(arr):
    omax = 0
    dp = [-1]* len(arr)

    dp[0] = 1

    for i in range(1, len(arr)):
        mx,j = 0,0
        while j < i:
            if arr[j] < arr[i]:
                if dp[j] > mx:
                    mx = dp[j]
            j += 1
        dp[i] = mx + 1

        if dp[i] > omax:
            omax = dp[i]

    return omax


arr = [10, 22, 9, 33, 50, 41, 60, 80, 9]
print(lis(arr))