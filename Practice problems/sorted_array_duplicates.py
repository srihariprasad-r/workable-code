def removeduplicates(nums):
    duplicate_dict = {}
    for i in nums:
        duplicate_dict[i] = nums.count(i)
    
    print(duplicate_dict)

    for k,v in duplicate_dict.items():        
        n = 0        
        if v > 2:
            while (v - n > 2 ):
                nums.remove(k)
                n += 1
    return len(nums)

nums = [0,0,1,1,1,1,2,3,3]
a = removeduplicates(nums)
print(a)


#nums.remove(1)
#print(nums)