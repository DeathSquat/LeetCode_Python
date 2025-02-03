class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
    
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
        
            # Check if complement exists in dictionary
            if complement in num_map:
                return [num_map[complement], i]
        
            # Store the index of the current number
            num_map[num] = i
        
