def largestsubarraysum(arr,k):
    rsum, mx, i, j = 0, 0, 0, 0
    while j < len(arr):
        rsum += arr[j]
        while rsum > k:
            rsum -= arr[i]
            i += 1
        if rsum == k:
            mx = max(mx, j - i + 1)
            j += 1
        elif rsum < k:
            j += 1

    return mx


arr = [4, 1, 1, 1, 2, 3, 2, 5]
k = 5 
print(largestsubarraysum(arr, k))