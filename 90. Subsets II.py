class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start, path):
            result.append(list(path))  # Add current subset to result
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue  # Skip duplicate elements
                
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # Remove last element to backtrack

        nums.sort()  # Sort to handle duplicates easily
        result = []
        backtrack(0, [])
        return result
