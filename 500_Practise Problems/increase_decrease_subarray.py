"""
Differences between number of increasing subarrays and decreasing subarrays in k sized windows
nums = {10, 20, 30, 15, 15}; 

Output: 3, 0 , -1
"""

def decreaseincreasearray(x, k):
    inc_count = 0
    dec_count = 0
    same_count = 0
    inc_dec_dict = {}    
    for i in range(0, len(x)):
        y = x[i:i+k]
        for j in range(len(y)-1):
            if y[j] < y[j + 1]:
                inc_count += 1
                inc_dec_dict.setdefault('inc', []).append(i)
            elif y[j] > y[j + 1]:
                dec_count -= 1
                inc_dec_dict.setdefault('dec', []).append(i)
            else:
                same_count = 1
                inc_dec_dict.setdefault('same', []).append(i)
    #print(inc_count, dec_count, same_count)
    print(inc_dec_dict)


             

x = [10, 20, 30, 15, 15] 
decreaseincreasearray(x, k=3)
