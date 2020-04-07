#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# 1. Restate the problem
# Using integers in an array, return the indices of two numbers that equal to a certain sum/target
# 2. Ask Clarifying Questions
#  Are the numbers sorted? Are there negative or positives?
# 3. State Assumptions
# I'll assume there are no repeated numbers and that they all are sorted
# 4a. Brainstorm Solutions
#Loop through the nums and determine if a is present in nums
# 4c. Discuss Tradeoffs
#It's an n^2 because of the loop and checking if a is present in nums

def twoSum(nums, target):
        
    for i in range(len(nums)):
        a = target - nums[i]
        if a in nums and i != nums.index(a):
            return([i, nums.index(a)])


nums = [6, 7, 8, 9, 10]
target = 13
print(twoSum(nums, target))

