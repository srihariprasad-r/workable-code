"""
Differences between number of increasing subarrays and decreasing subarrays in k sized windows
nums = {10, 20, 30, 15, 15}; 

Output: 3, 0 , -1
"""

def decreaseincreasearray(x, k):
    inc_count = 0
    dec_count = 0
    same_count = 0
    for i in range(0, len(x)):
        y = x[i:i+k]
        for j in range(len(y)-1):
            if y[j] < y[j + 1]:
                inc_count += 1
            elif y[j] > y[j + 1]:
                dec_count += 1
            else:
                same_count = 1
    print(inc_count, dec_count, same_count)

             

x = [10, 20, 30, 15, 15] 
decreaseincreasearray(x, k=3)
