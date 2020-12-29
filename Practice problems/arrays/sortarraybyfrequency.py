from functools import cmp_to_key

def sortarraybyfrequency(arr):
    map_freq = {}

    for i in arr:
        if not(map_freq.get(i)):
            map_freq[i] = arr.count(i)

    def sortfunc(n1, n2):
        freq1 = map_freq.get(n1)
        freq2 = map_freq.get(n2)
        if (freq1 != freq2): 
            return freq2 - freq1
        else: 
            return n1 - n2 

    return sorted(arr, key=cmp_to_key(sortfunc))

arr = [10, 7, 10, 11, 10, 7, 5, 6]
print(sortarraybyfrequency(arr))