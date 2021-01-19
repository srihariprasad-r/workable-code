def nearestgreaterelement(arr):
    result = [0] * (len(arr))
    for i in range(len(arr)):
        stck = []
        j = len(arr) - 1
        while j > i:
            stck.append(arr[j])
            j -= 1
        
        cnt = len(stck)

        while cnt > 0 :
            if arr[i] < stck[-1]:
                result[i] = stck[-1]
                break
            else:
                stck.pop(-1)
                cnt -= 1

        if len(stck) == 0: 
            result[i] = -1
    
    return result

arr = [1, 3, 0, 0, 1, 2, 2]
print(nearestgreaterelement(arr))