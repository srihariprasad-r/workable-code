def maxsumsubarray(arr,k):
    i, j, rsum, msum = 0, 0, 0, 0
    while j < len(arr):
        rsum += arr[j]
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            msum = max(msum, rsum)
            rsum -= arr[i]
            i += 1
            j += 1
    return msum

arr = [3,2,5,4,1,20]
k = 3
print(maxsumsubarray(arr, k))