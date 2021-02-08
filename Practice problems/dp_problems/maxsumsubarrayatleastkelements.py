def maxsumsubarrayatleastkelements(arr,k=0):
    rbest = [0] * len(arr)
    tbest = 0
    cbest_arr = []
    cbest_sum = 0
    obest_sum = 0
    i = 0

    while i < len(arr):
        cbest_sum += arr[i]
        if cbest_sum > arr[i]:
            cbest_arr.append(arr[i])
        else:
            cbest_sum = arr[i]
            cbest_arr = []
            cbest_arr.append(arr[i])
        rbest[i] = cbest_sum
        
        if obest_sum < cbest_sum:
            obest_arr = []
            obest_sum = cbest_sum
            obest_arr = cbest_arr[:]

        i += 1
            
    for i in range(len(arr)-k+1):
        tsum = sum(arr[:i+k])
        if tsum > tbest :
            tbest = tsum
        elif tsum + rbest[i-1] > tbest:
            tbest = tsum + rbest[i-1]
            
    return tbest
            

arr = [2, 3, 1, -7, 6, -5, -4, 4, 3, 3, 2, -9, -5, 6, 1, 2, 1, 4]
print(maxsumsubarrayatleastkelements(arr, 4))