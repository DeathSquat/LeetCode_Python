class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start):
            # If we've reached the end of the array, store the permutation
            if start == len(nums):
                result.append(nums[:])  # Make a copy of nums
                return
            
            used = set()  # Track numbers already used at this level
            for i in range(start, len(nums)):
                if nums[i] in used:  # Skip duplicates
                    continue
                used.add(nums[i])
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse with the next index as the start
                backtrack(start + 1)
                # Backtrack (undo the swap)
                nums[start], nums[i] = nums[i], nums[start]
        
        result = []
        nums.sort()  # Sort to handle duplicates easily
        backtrack(0)
        return result
