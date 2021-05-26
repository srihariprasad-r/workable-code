def maxsumnonoverlappingsubarray(arr,k):
    csum_1 = 0
    maxsum_1 = -float('inf')
    loc_1 = []

    csum_2 = 0
    maxsum_2 = -float('inf')
    loc_2 = []
    
    csum_3 = 0
    maxsum_3 = -float('inf')
    loc_3 = []
    
    for i in range(len(arr)-k):
        j = i + k
        m = j + k
        csum_1 = sum(arr[i:j])
        csum_2 = csum_1 + sum(arr[j:j+k])
        csum_3 = csum_2 + sum(arr[m:m+k])
        
        if csum_1 > maxsum_1:
            maxsum_1 = csum_1
            loc_1 = [i]
            
        if csum_2 > maxsum_2:
            maxsum_2 = csum_2
            loc_2 = [i,j]
            
        if csum_3 > maxsum_3:
            maxsum_3 = csum_3
            loc_3 = [i,j,m]
            
    return sum(arr[loc_3[0]:loc_3[2]+k])


arr = [1, 2, 1, 2, 6, 7, 5, 1]
print(maxsumnonoverlappingsubarray(arr,2))