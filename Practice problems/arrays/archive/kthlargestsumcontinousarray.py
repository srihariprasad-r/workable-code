result = []

def kthlargestcontinoussum(arr,k):
    csum = 0
    for i in range(len(arr)):
        start = i + 1
        csum = arr[i]
        while start < len(arr) :
            csum += arr[start]
            start += 1
        result.append(csum)

    result.sort(key=lambda  x: -x)
    return result[k-1]

arr = [20, -5, -1]
print(kthlargestcontinoussum(arr,1))