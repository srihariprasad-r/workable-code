from collections import deque

q = deque()

def nonoverlapmaxsum(arr,k):
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
                q.appendleft(maxfar)
            elif max_sum < 0:
                max_sum = 0
                s = start +1
            start += 1

    while len(q) > 0 and len(q) > k:
        q.pop()

    return q

arr = [5, 1, 2, -6, 2, -1, 3, 1]
print(nonoverlapmaxsum(arr, 2))