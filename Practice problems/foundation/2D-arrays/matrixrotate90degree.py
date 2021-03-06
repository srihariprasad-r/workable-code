def matrixrotation(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr[0])):
            temp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = temp
            
    
    for i in range(len(arr)):
        lindex = 0
        rindex = len(arr) -1
        
        while lindex < rindex:
            tmp =arr[i][lindex]
            arr[i][lindex] = arr[i][rindex]
            arr[i][rindex] = tmp
            
            lindex += 1
            rindex -= 1
            
    return arr
            


arr = [
 [1, 2, 3],
 [20, 30, 40],
 [50, 60, 70]
]
print(matrixrotation(arr))