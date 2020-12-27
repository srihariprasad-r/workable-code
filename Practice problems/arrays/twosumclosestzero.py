result = []

def tripletclosestsum(arr, csum):
    arr.sort()
    closestsum = float('inf')
    for i in range(len(arr)+1):
        start = i+1
        while start < len(arr):
            rsum = abs(abs(arr[i]) - abs(arr[start]))
            if abs(csum - rsum) < abs(csum - closestsum):
                closestsum = rsum
                result.append([arr[i], arr[start]])
            else:
                start += 1
    
    return closestsum
        


arr = [1, 60, -10, 70, -80, 85] 
print(tripletclosestsum(arr, 6))
print(result)