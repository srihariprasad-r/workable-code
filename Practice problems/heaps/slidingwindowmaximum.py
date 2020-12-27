from collections import deque

q = deque()
result = []

def slidingwindowmaximum(arr,k):
    for i in range(0,k):
        while len(q) > 0 and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)
    result.append(q[0])
    
    for i in range(k, len(arr)):
        while len(q) > 0 and q[0] <= i - k:
            q.popleft()
        while len(q) > 0 and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)
        result.append(q[0])

k = 3
array = [12, 1, 78, 90, 57, 89, 56]
slidingwindowmaximum(array, k)
print([array[i] for i in result])