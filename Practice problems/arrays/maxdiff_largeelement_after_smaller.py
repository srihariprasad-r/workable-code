def maxdiff_largeelement_after_smaller(arr):

    curdiff = 0
    maxdiff = -float('inf')
    
    for i in range(len(arr)):
        j = i + 1
        while j < len(arr):
            if arr[i] < arr[j]:
                curdiff = arr[j] - arr[i]
                if curdiff > maxdiff:
                    maxdiff = curdiff
                    start = i
                    end = j

            j += 1

    return arr[end] - arr[start]

arr = [7, 9, 5, 6, 3, 2]
print(maxdiff_largeelement_after_smaller(arr))