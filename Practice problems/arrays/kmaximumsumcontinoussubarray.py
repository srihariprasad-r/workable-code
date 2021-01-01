
result = []

def kmaximumsum(arr,k):
    for i in range(len(arr)):
        max_sum, rsum, start  = 0, 0, i
        while start < len(arr):
            rsum += arr[start]
            if rsum > max_sum:
                max_sum = rsum
            start += 1
        result.append(max_sum)
    return sorted(result, key=lambda x: -x)[:k]


arr = [4, -8, 9, -4, 1, -8, -1, 6]
print(kmaximumsum(arr, k=4))