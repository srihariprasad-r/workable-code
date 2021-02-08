def kadanealgorithm(arr):
    cbest_arr = []
    cbest_sum = 0
    obest_sum = 0
    obest_arr = []
    i = 0

    while i < len(arr):
        if cbest_sum > arr[i]:
            """
            if current element is less than current running sum, keep adding current value to current best array
            and update its current best sum
            """
            cbest_sum += arr[i]
            cbest_arr.append(arr[i])
        else:
            """
            if current element is greater than current running sum, clear the current best array and add current element to current best array
            and assign its current best sum to current element
            """
            cbest_sum = arr[i]
            cbest_arr = []
            cbest_arr.append(arr[i])
        
        if obest_sum < cbest_sum:
            """
            if current element is greater than overall running sum, clear the overall best array and add current best array to overall best array
            and assign its current best sum to overall best sum
            """
            obest_arr = []      #clear off existing values
            obest_sum = cbest_sum
            obest_arr = cbest_arr[:]
            
        i += 1
            
    return obest_sum

arr = [4, 3 -2, 6, -14, 7, -1, 4, 5, 7, -10, 2, 9, -10, -5, -9, 6, 1]
print(kadanealgorithm(arr))
