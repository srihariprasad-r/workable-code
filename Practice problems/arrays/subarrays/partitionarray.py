def partitionarray(arr):
    res = []
    totalsum = sum(arr)
    cursum = 0
    
    for i in range(len(arr)):
        cursum += arr[i]
        
        if totalsum - cursum == cursum:
            return i
            

arr = [6, -4, -3, 2, 3]
idx = partitionarray(arr)
print(arr[0:idx+1])
print(arr[idx+1:])