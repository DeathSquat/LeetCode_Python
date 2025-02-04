class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start, path):
            result.append(path[:])  # Add current subset to result
            
            for i in range(start, len(nums)):
                path.append(nums[i])  # Choose
                backtrack(i + 1, path)  # Explore
                path.pop()  # Un-choose
        
        backtrack(0, [])
        return result
