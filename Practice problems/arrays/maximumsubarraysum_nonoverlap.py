def nonoverlapmaxsum(arr):
    maxfar, end, s, st  = float('-inf'), 0, 0, 0
    for i in range(len(arr)):
        start= i
        max_sum = 0
        while start < len(arr):
            max_sum += arr[start]
            if max_sum > maxfar:
                maxfar = max_sum
                st = s
                end = start
            elif max_sum < 0:
                max_sum = 0
                s = start +1
            start += 1

    return maxfar, arr[st: end+1]

arr = [4, 1, 1, -1, -3, -5, 6, 2, -6, -2]
print(nonoverlapmaxsum(arr))