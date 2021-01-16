dct = {}
def largestsubarraysum(arr,k):
    rsum, dsum, j = 0, 0, 0
    while j < len(arr):
        rsum += arr[j]
        if rsum == k:
            return arr[0:j]
        dsum = rsum - k
        if dsum in dct:
            return arr[dct[dsum] + 1 : j + 1]
        else:
            dct[rsum] = j
        j += 1
            

arr = [4, 2, -5, 3, 1,  8]
k = -1
print(largestsubarraysum(arr, k))