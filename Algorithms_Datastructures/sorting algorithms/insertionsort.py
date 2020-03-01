def insertionsort(array):
    for i in range(1, len(array)):
        for j in range(i-1, -1 , -1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            else:
                break
    
    return array

array = [6,2,1,3,4]
print(insertionsort(array))