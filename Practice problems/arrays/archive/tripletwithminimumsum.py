result = []

def tripletminimumsum(arr):
    minsum = float('inf')
    for i in range(len(arr)):
        print(arr[i])
        start = i + 1
        end = len(arr) - 1
        while start < end:
            rsum = arr[i] + arr[start] + arr[end]
            if rsum < minsum:
                minsum = rsum
                result.append([arr[i], arr[start], arr[end]])
            if rsum >= minsum:
                start += 1

    return minsum


arr = [1, 2, 3, 4, -1, 5, -2]
print(tripletminimumsum(arr))
print(result)

