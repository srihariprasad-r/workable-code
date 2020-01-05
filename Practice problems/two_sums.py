def twoSum(nums, target):
    dict = {}
    lookup = 0
    for i in range(len(nums)):
        lookup = target - nums[i]
        if lookup not in nums:
            dict[nums[i]] = i
        else:
            print [dict[nums[i]], i]

    #print(dict)
    #for i in dict.values():
    #    return i

nums = [3,2,4]
a = twoSum(nums, 6)
print(a)