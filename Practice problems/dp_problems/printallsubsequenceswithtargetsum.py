from collections import deque

d= deque()

def targetsum(arr, tsum):
    dp = [[0 for i in range(tsum+1)] for j in range(len(arr))]

    for i in range(len(arr)):
        for j in range(tsum+1):
            if j == 0:
                dp[i][j] = 1
            elif i == 0 :
                dp[i][j] = 0
            else:
                if j < arr[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-arr[i]])

    d.append((len(arr), tsum, ""))
    
    while len(d) > 0:
        el = d.popleft()
        i, j, stng = el[0], el[1], el[2]
        if i == 0 and j == 0:
            print(stng)
        else:
            if j >= arr[i-1]:
                incl = dp[i-1][j-arr[i-1]]
        
            if incl:
                d.append((i-1, j-arr[i-1], str(arr[i-1]) + " " + stng))
                
            excl = dp[i-1][j]
            if excl:
                d.append((i-1, j, stng))
            
            
    
    
arr = [4, 2, 7, 1, 3]
tsum = 10
print(targetsum(arr, tsum))