def search_index(nums, target):
    a = 0
    b = len(nums) -1

    while(a < b):
        mid = (a + b) /2
        print("value of mid:", mid)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            a = mid + 1
            print("low:", a)
        elif nums[mid] > target:
            b = mid - 1
            print("high:", b)
    
    return a

nums = [1,3]
b_o= search_index(nums, 2)
print(b_o)
