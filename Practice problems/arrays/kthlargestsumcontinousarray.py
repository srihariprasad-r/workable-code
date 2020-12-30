def kthlargestcontinoussum(arr):
    csum, max_sum = 0, float('-inf')
    for i in range(len(arr)):
        start = i + 1
        csum = arr[i]
        while start < len(arr) :
            csum += arr[start]
            start += 1
        if max_sum < csum:
            max_sum = csum

    return max_sum

arr = [20, -5, -1]
print(kthlargestcontinoussum(arr))