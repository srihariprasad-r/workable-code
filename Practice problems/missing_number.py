def missing_number(nums):
    n = len(nums)
    return n*(n+1)/2 - sum(nums)

nums = [0]
a = missing_number(nums)
print(a)
