# 🟡 Question – Second Largest Distinct Element
# 📝 Problem Statement

# Given an integer array nums, return the second largest distinct element in the array.

# If the second largest distinct element does not exist, return -1.

# 🔹 Example 1

# Input:

nums = [3, 7, 2, 9, 5]
if len(nums)< 2:
    print(-1)
else:
    
    if nums[1]>nums[0]:
        large= nums[1]
        sec_large=nums[0]
    else:
        large=nums[0]
        sec_large=nums[1]
        
    for i in range(2,len(nums)):
        if nums[i] > large:    #2>7
            sec_large = large
            large = nums[i]
        
        elif nums[i]>sec_large:#2>3
            sec_large = nums[i]
            
            

# print(large)
print(sec_large)
        
    
    