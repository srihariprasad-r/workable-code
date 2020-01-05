def sub_array(nums):
    table_list = []
    table_list.append(nums[0])
    max_value = nums[0]
    for i in range(1,len(nums)):
        max_value = max(nums[i]+max_value, nums[i])
        table_list.append(max_value)

    return max(table_list)

nums = [-2,1,-3,4,-1,2,1,-5,4]
a = sub_array(nums)
print(a)
