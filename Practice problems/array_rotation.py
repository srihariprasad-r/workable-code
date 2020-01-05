arr = [1, 2, 3, 4, 5, 6, 7]

def rotation(arr, n):
    return arr[-n:] + arr[:-n]

rs = rotation(arr,2)
print(rs)

