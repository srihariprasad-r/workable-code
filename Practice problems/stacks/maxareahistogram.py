def maxareahistogram(arr):
    result_right = [0] * len(arr)
    result_left = [0] * len(arr)
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

    return result_left, result_right


arr = [6, 2, 5, 4, 5, 1, 6]
print(maxareahistogram(arr))