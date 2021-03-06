result = []

def tripletclosestsum(arr, csum):
    arr.sort()
    closestsum = float('inf')
    for i in range(len(arr)-2):
        start = i + 1
        end = len(arr) - 1
        while start < end:
            rsum = arr[i] + arr[start] + arr[end]
            if abs(csum - rsum) < abs(csum - closestsum) :
                closestsum = rsum
                result.append([arr[i], arr[start], arr[end]])
            if rsum < csum:
                start += 1
            else:
                end -= 1
    return closestsum
                

target_sum = 1
arr = [ -1, 2, 1, -4]
res = tripletclosestsum(arr, target_sum)
print(result, res)