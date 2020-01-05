def merge_sorted_array(num1,m,num2,n):
    new_array = nums1[:-m]
    for i in nums2:
        new_array.append(i)
    return sorted(new_array)


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

#a = merge_sorted_array(nums1,3,nums2,3)
#print(a)

sorted(nums1)
print(nums1)
