"""
Input : {1, 0, 1, 1, 1, 0, 0}
Output : 1 to 6

Input : {0, 0, 1, 1, 0}
Output: 0 to 3 or 1 to 4 
"""

def equalSubArray(array, n):
    maxlen = -1
    startindex = 0
    for i in range(0, n-1):
        if array[i] == 0:
            sum = -1
        else:
            sum = 1
        for j in range(i+1, n):
            if array[j] == 0:
                sum += -1
            else:
                sum += 1
            if (sum == 0 and maxlen < j-i+1):
                maxlen = j-i+1
                startindex = i
    
    return maxlen, startindex

       




array = [1, 0, 1, 1, 1, 0, 0]
n = len(array)
equalSubArray(array, n)