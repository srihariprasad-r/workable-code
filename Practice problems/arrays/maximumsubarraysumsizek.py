from collections import deque

q = deque()

def maxsubarraysum_sizek(arr,k):
    rsum = 0
    for i in range(0, k):
        rsum += arr[i]
    q.append(rsum)

    for i in range(1, len(arr)-k+1):
        rsum, start = 0, i
        cnt = 0
        while cnt < k :
            rsum += arr[start]
            start += 1
            cnt += 1

        while len(q) > 0 and q[-1] < rsum:
            q.pop()
            q.append(rsum)

    return q

arr = [3,2,5,4,1,20]
k = 3
print(maxsubarraysum_sizek(arr, k))
