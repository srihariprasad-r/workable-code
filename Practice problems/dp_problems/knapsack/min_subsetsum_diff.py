"""
Notes:
1. To find minimum subsetsum difference, we do decide range of the array which is sum of all elements
2. Then we find the subsets which have range in the array
3. So last row of the dp will show the subsets and we take first n/2 elements as:
    s2 = {...} can be derived from range - s1
    abs(s2 - s1) => abs(range-s1-s1) => abs(range-2s1)
4. We apply above formula and decide which has minimum difference
"""

import sys

def min_subset_diff(arr):
    csum = 0
    newlist = []
    for i in range(len(arr)):
        csum += arr[i]

    subset = subsetsum(arr, csum)
    elements = subset[-1]
    print(subset)
    mn = sys.maxsize

    for i in range(len(elements)):
        if i < len(elements)//2 and elements[i]:
            newlist.append(i)
    
    for i in range(len(newlist)):
        mn = min(mn, (csum-2*newlist[i]))

    return mn
                

def subsetsum(arr, tsum):
    dp = [[False for x in range(tsum + 1)] for y in range(len(arr)+1)]

    for j in range(len(arr)+1):
        dp[j][0] = True

    for i in range(1,len(arr)+1):
        for j in range(1,tsum + 1):
            if j >= arr[i-1]:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp


arr = [1, 2, 7]
print(min_subset_diff(arr))