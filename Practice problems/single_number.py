def single_number(nums):
    dct = {i : nums.count(i) for i in nums}
    for k,v in dct.items(): if v == 1: return k

nums = [2,2,1]
a = single_number(nums)
print(a)
