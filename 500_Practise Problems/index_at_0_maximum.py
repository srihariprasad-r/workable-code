"""
Input = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
Output = 9
"""

def maximum_index_at_0(array):    
    prev_zero = 0
    prev_cnt = 0
    max_cnt = 0
    for i in range(0,len(array)):
        if array[i] == 0 :
            if i - prev_zero  > max_cnt:
                if max_cnt > prev_cnt:
                    max_cnt = i - prev_zero
                    prev_zero = i
                    prev_cnt = max_cnt
                    print(max_cnt, prev_zero)

array = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
maximum_index_at_0(array)