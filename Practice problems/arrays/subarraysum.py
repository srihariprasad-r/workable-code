from collections import deque

q = deque()

def subarraysum(arr, tsum):
    cursum = 0
    for i in range(len(arr)):
        cursum += arr[i]
        while len(q) > 0 and cursum > tsum:
            el = q.popleft()
            cursum -= el
        if tsum - arr[i] > 0:
            q.append(arr[i]) 
        
        if cursum == tsum:
            return [q[i] for i in range(len(q))]
    
    return 0


tsum = 33
arr = [1, 4, 20, 3, 10, 5]
print(subarraysum(arr, tsum))