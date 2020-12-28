result = []

def countpairswithsum(arr,tsum):
    csum = 0
    for i in range(len(arr)):
        start = i + 1
        while start < len(arr):
            csum = arr[i] + arr[start]
            if csum - tsum == 0:
                result.append([arr[i], arr[start]])
                break
            else:
                start += 1
    return result


arr = [1, 5, 7, -1]
tsum = 6
print(countpairswithsum(arr, tsum))