#Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# 1. Restate the problem
# Using an array of integers, remove the duplicates so they appear only once, and return the new length.
# 2. Ask Clarifying Questions
#  Will there be negative numbers? Positives? Are they sorted?
# 3. State Assumptions
# I'll assume they are all positive unsorted numbers.
# 4a. Brainstorm Solutions
#Loop through numbers and set a count. Compare numbers with a nested loop and append the count to output to return the answer
# 4c. Discuss Tradeoffs
#It's would be n^2 because of the nested  loop 


def smallerNumbersThanCurrent(nums):
    output = []
    for i in range(len(nums)):
        count = 0
        for m in range(len(nums)):
            if nums[m] < nums[i] and m!= i:
                count += 1
        output.append(count)
                
    return output
            
        
        
        
nums = [8, 4, 4, 6, 1]
print(smallerNumbersThanCurrent(nums))