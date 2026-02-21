# 📝 Problem Statement
# Given an integer array nums, return the largest element in the array.
# You must solve it in O(n) time complexity.

# 🔹 Example 1:
# Input:
# nums = [3, 7, 2, 9, 5]

# solution:-

nums = [3, 7, 2, 9, 5]
lar= 3
for i in nums:
    if i >= lar:
        lar= i
print(lar)    

    
    