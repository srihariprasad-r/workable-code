result = []

def tripletsum(arr, tsum):
    arr.sort()
    for i in range(len(arr)):
        currentsum = tsum - arr[i]
        start = i+1
        end = len(arr) - 1
        while start < end:
            if arr[start] + arr[end] == currentsum:
                found = [arr[i], arr[start], arr[end]]
                result.append(found)
                start += 1
                end -= 1
            elif arr[start] > currentsum:
                start += 1
            else:
                end -= 1

targetsum = 1
array = [1, 2, -3, 4, -2, -1]
tripletsum(array, targetsum)
print(result)   # [[-2, -1, 4], [-2, 1, 2]]