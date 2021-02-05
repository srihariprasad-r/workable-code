from collections import deque

q = deque()

def mincostpath(arr):
    dp = [[0 for i in range(len(arr))] for j in range(len(arr))]
    
    dp[-1][-1] = 1
    
    for i in range(len(arr)-1, -1, -1):
        for j in range(len(arr)-1, -1, -1):
            if i == len(arr)-1 : 
                if j < len(arr)-1:
                    dp[i][j] = dp[i][j+1] + arr[i][j]
            elif j == len(arr)-1:
                if i < len(arr)-1:
                    dp[i][j] = dp[i+1][j] + arr[i][j]
            else:
                if dp[i+1][j] < dp[i][j+1]:
                    dp[i][j] = arr[i][j] + dp[i+1][j]
                else:
                    dp[i][j] = arr[i][j] + dp[i][j+1]
    
    q.append((0, 0, str(arr[0][0])))
    result = []
    
    while len(q) > 0:
        el = q.pop()
        i_index, j_index, strn = el[0], el[1], el[2]
        if i_index == len(dp) - 1 and j_index == len(dp[0]) -1:
            result.append(strn)
        elif i_index == len(dp) - 1:
            q.append((i_index, j_index+1, str(arr[i_index][j_index+1])+'->'+strn))
        elif j_index == len(dp[0]) - 1:
            q.append((i_index+1, j_index, str(arr[i_index+1][j_index])+'->'+strn))
        else:
            if dp[i_index+1][j_index] < dp[i_index][j_index+1]:
                q.append((i_index+1, j_index, str(arr[i_index+1][j_index])+'->'+strn))
            elif dp[i_index+1][j_index] > dp[i_index][j_index+1]:
                q.append((i_index, j_index+1, str(arr[i_index][j_index+1])+'->'+strn))
            else:
                q.append((i_index+1, j_index, str(arr[i_index+1][j_index])+'->'+strn))
                q.append((i_index, j_index+1, str(arr[i_index][j_index+1])+'->'+strn))
                
    return result  
    

arr = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]
print(mincostpath(arr))