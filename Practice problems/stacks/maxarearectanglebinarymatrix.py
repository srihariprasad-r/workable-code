"""
Find maximum area of rectangular binary matrix.
This follows same approach as MAH(max-area histogram) problem
1.
[
    [....] -> 1st level 
    [....] -> 2nd level (sum all elements column wise with above row)
    ....
]
2.One condition is, when an element is 0 at the current level, reset the sum to zero as there is no ground level
3. Run MAH at all levels of the matrix and derive the max and then do total max
"""
def maxareabinarymatrix(arr):
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

        while k < i:
            stck_left.append(k)
            k += 1
        
        cnt_right = len(stck_right)
        cnt_left = len(stck_left)

        while cnt_right > 0:
            if arr[i] > arr[stck_right[-1]]:
                result_right[i] = stck_right[-1]
                break
            stck_right.pop(-1)
            cnt_right -= 1

        while cnt_left > 0:
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

    return max([width[i] * arr[i] for i in range(len(arr))])

def main(arr):
    tmp = []
    mx = []
    for i in range(len(arr)):
        tmp.append(arr[0][i])
    maxel = maxareabinarymatrix(tmp)
    mx.append(maxel)

    for i in range(1, len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 0:
                tmp[j] = 0
            else:
                tmp[j] = tmp[j] + arr[i][j]
        maxel = maxareabinarymatrix(tmp)
        mx.append(maxel)

    return mx


arr = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]
print(main(arr))