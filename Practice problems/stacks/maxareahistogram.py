"""
Find maximum area of histogram:
1. Calculate NSL(nearest smallest left) for each element
2. Calculate NSR(nearest smallest right) for each element
3. For both calculations,
    1. when current element is last(for NSR), take len(arr) as NSR(right side) since there is no building to compare
    2. when current element is first(for NSL), take -1 as NSL(left side) since there is no building to compare
4. From this, two arrays are derived and to find width of each element,
    width[i] = right[i] - left[i] - 1
we do reduce -1 as left and right are boundaries till we can find area and we should neglect the NSL/NSR as they are smaller than current element
5. Multiply array element with width to get the area
"""

def maxareahistogram(arr):
    result_right = [0] * len(arr)
    result_left = [0] * len(arr)
    width = [0] * len(arr)
    for i in range(len(arr)):
        stck_right = []
        stck_left = []

        j = len(arr) - 1
        k = 0

        while j > i:
            stck_right.append(j)
            j -= 1
        cnt_right = len(stck_right)

        while k < i:
            stck_left.append(k)
            k += 1
        cnt_left = len(stck_left)

        while cnt_right > 0 :
            if arr[i] > arr[stck_right[-1]]:
                result_right[i] = stck_right[-1]
                break
            stck_right.pop(-1)
            cnt_right -= 1

        while cnt_left > 0 :
            if arr[i] > arr[stck_left[-1]]:
                result_left[i] = stck_left[-1]
                break
            stck_left.pop(-1)
            cnt_left -= 1

        if len(stck_right) == 0:
            result_right[i] = len(arr)
        
        if len(stck_left) == 0:
            result_left[i] = -1

    for i in range(len(result_right)):
        width[i] = result_right[i] - result_left[i] - 1

    return [arr[i]*width[i] for i in range(len(arr))]

arr = [6, 2, 5, 4, 5, 1, 6]
print(maxareahistogram(arr))