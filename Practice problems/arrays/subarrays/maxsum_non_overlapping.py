def maxsumnonoverlappingsubarray(arr,k):
    csum_1 = 0
    maxsum_1 = -float('inf')
    loc_1 = []
    
    for i in range(len(arr)-k):
        j = i + k
        csum_1 = sum(arr[i:j])
        
        if csum_1 > maxsum_1:
            maxsum_1 = csum_1
            loc_1 = [i]
            
    return sum(arr[loc_1[0]:loc_1[0]+k])


arr = [1, 2, 1, 2, 6, 7, 5, 1]
print(maxsumnonoverlappingsubarray(arr,2))