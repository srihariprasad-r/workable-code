# incorrect solution

from collections import deque

q = deque()

def printalllis(arr):
    omax, oindex = 0, 0
    dp = [0] * len(arr)

    dp[0] = 1

    for i in range(1, len(arr)):
        mx, j = 0, 0 
        while j < i:
            if arr[j] < arr[i]:
                if mx < dp[j]:
                    mx  = dp[j]
            j += 1
        dp[i] =  mx + 1

    for i in range(len(dp)):
        if omax < dp[i]:
            omax = dp[i]
            oindex = i

    q.append(oindex)
    result = []

    while len(q) > 0:
        curList = []
        for _ in range(len(q)):
            val = q.popleft()
            j = val - 1
            if arr[val] > arr[j] and j > 1:
                q.append(j)
            curList.append(arr[j])
        result.append(curList)

    print(result)
            


arr = [10, 22, 9, 33, 50, 41, 60, 80, 9]
print(printalllis(arr))