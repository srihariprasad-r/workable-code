"""
Find no. of days prior to current day 
where stock price was lesser or equal to current price
"""
def stockspan(arr):
    result = [0] * len(arr)
    for i in range(len(arr)):
        stck = []
        j = 0
        while j < i:
            stck.append(arr[j])
            j += 1

        cnt = len(stck)
        var = 1

        while cnt > 0:
            if arr[i] > stck[-1]:
                var += 1
            stck.pop(-1)
            cnt -= 1
        result[i] = var
    
    return result


arr = [100, 80, 60, 70, 60, 75, 85]
print(stockspan(arr))