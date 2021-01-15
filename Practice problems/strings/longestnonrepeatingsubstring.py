# incorrect solution, needs rework

from collections import deque

q = deque()

def longestnonrepeatingstring(str):
    start, cur, cnt  = 0, 0, 0

    for _ in range(1):
        cur += 1
        q.append(str[0])

    while cur < len(str):
        cur += 1
        while q and q.count(str[cur]) > 0:
            q.popleft()
            start += 1
        q.append(str[cur])
        cnt = max(cnt, cur - start +1)

    return cnt

str = 'geeksforgeeks'
print(longestnonrepeatingstring(str))