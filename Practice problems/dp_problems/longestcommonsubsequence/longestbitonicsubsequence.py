def longestbitonic(arr):
    smax = 0
    lis = [0] * len(arr)
    lds = [0] * len(arr)

    """
    For longest increasing subsequence, we traverse from left to right

    arr: [1, 2, 3, 4]

    To get LDS for 2, we consider {1,2}
    Similarly, for 3, we consider {1,2,3}
    """
    for i in range(len(arr)):
        mx, j = 0, 0
        while j < i:
            if arr[j] < arr[i]:
                if lis[j] > mx:
                    mx = lis[j]
            j += 1
        lis[i] = mx + 1

    """
    For longest decreasing subsequence, we traverse from right to left

    arr: [1, 2, 3, 4]

    To get LDS for 3, we consider {3, 4}
    Similarly, for 2, we consider {2, 3, 4}
    """
    for i in range(len(arr)-1, -1, -1):
        mx, j = 0, i
        while j < len(arr):
            if arr[j] < arr[i]:
                if lds[j] > mx:
                    mx = lds[j]
            j += 1
        lds[i] = mx + 1

    
    for i in range(len(lis)):
        smax = max(smax, lis[i] + lds[i] -1)

    return smax

arr =  [10, 22, 9, 33, 21, 50, 41, 60, 80, 3]
print(longestbitonic(arr))