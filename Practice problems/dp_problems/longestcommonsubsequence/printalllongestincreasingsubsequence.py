"""
To get all longest increasing subsequences,

we get the maximum length of subsequence and store it along with index which occurs at maximum.
Then we pop that element and we check if arr[index] < arr[maxindex] and also if index = maxindex -1 to check if its prior element
We append those array values to a string

Queue will look similar to below:
deque([(6, 7, '80')])
deque([(5, 6, '80->60')])
deque([(4, 5, '80->60->41'), (4, 4, '80->60->50')])
deque([(4, 4, '80->60->50'), (3, 3, '80->60->41->33')])
deque([(3, 3, '80->60->41->33'), (3, 3, '80->60->50->33')])
deque([(3, 3, '80->60->50->33'), (2, 1, '80->60->41->33->22')])
deque([(2, 1, '80->60->41->33->22'), (2, 1, '80->60->50->33->22')])
deque([(2, 1, '80->60->50->33->22'), (1, 0, '80->60->41->33->22->10')])
deque([(1, 0, '80->60->41->33->22->10'), (1, 0, '80->60->50->33->22->10')])
"""

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

    q.append((omax, oindex, str(arr[oindex]) + ""))

    while len(q) > 0:
        output = q.popleft()
        val, index, stn = output[0], output[1], output[2]
        if index == 0:
            print(stn)
        else:
            for j in range(index-1, -1, -1):
                if arr[j] < arr[index] and dp[j] == val - 1:
                    q.append((dp[j],j , stn + "->" +  str(arr[j])))


arr = [10, 22, 9, 33, 50, 41, 60, 80, 9]
printalllis(arr)