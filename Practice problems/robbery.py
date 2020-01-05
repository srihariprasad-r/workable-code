def rob(nums):
    dp = []
    if nums is None:
        return 0
    elif len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])
    elif len(nums) > 2:
        dp.insert(0,1)
        dp.insert(1,max(nums[0], nums[1]))
        for i in range(2,len(nums)):
            dp.insert(i,max(nums[i] + dp[i-2], dp[i-1]))
                
        print(dp)        
        return dp[-1]

nums = [2,7,9,3,1]
rob(nums)