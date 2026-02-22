# Pattern: Counting While Traversing
# 📝 Problem Statement (LeetCode Style)

# Given an integer array nums, return the number of even numbers in the array.

# You must solve it in O(n) time.

# 🔹 Example 1

# Input:

nums = [1, 2, 3, 4, 6]

even =0
for i in nums:
    if i %2 == 0 :
        
        print(f"the evne number is {i}")
        even +=1
print("the total number of even numbers is :-",even)  
