"""
Differences between number of increasing subarrays and decreasing subarrays in k sized windows
nums = {10, 20, 30, 15, 15}; 

Output: 3, 0 , -1
"""

def decreaseincreasearray(x, k):
    inc_lis = [1] * k
    dec_lis = [1] * k
    same_lis = [1] * k
    window_dict = {}
    inc_count= 0 
    dec_count= 0 
    same_count = 0

    for i in range(0, len(x)):
        window_dict[i] = x[i:i+k]

    print(window_dict)

    for z , v in window_dict.items():
        for i in range(len(v)):
            for j in range(0, i):
                if v[i] > v[j] and inc_lis[i] < inc_lis[j] + 1:
                    inc_lis[i] += 1 
                elif v[i] < v[j] and dec_lis[i] > dec_lis[j] - 1:
                    dec_lis[i] -= 1                     
            
    print(inc_lis, dec_lis)
    #print(window_dict)   
    #print(inc_lis, dec_lis, same_lis)
    #print(inc_count, dec_count, same_count)


             

x = [10, 20, 30, 15, 15] 
decreaseincreasearray(x, k=3)
