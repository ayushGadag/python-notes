# 🟡 Question 3 – Check if Array is Sorted
# Pattern: Comparison with Previous Element
# 📝 Problem Statement (LeetCode Style)

# Given an integer array nums, return True if the array is sorted in non-decreasing order, otherwise return False.

# Non-decreasing means:
# Every element should be greater than or equal to the previous element.

# 🔹 Example 1

# Input:

num = [1, 2, 3, 4, 5]
is_sorted=True

for i in range(1,len(num)):
    if num[i] < num[i-1]:
         is_sorted = False
         break
        
print(is_sorted)
        
    
    
     


     
        

