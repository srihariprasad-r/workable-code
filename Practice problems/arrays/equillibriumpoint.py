def equillibrium(arr):
    tsum = sum(arr)
    sum_so_far = 0
    for i in range(len(arr)):
        tsum -= arr[i]
        if tsum == sum_so_far:
            return arr[i]
        sum_so_far += arr[i]


arr =[1,6,7,0,7]
print(equillibrium(arr))