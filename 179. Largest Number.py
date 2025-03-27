from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Convert numbers to strings for comparison
        nums = list(map(str, nums))
        
        # Custom comparator: Sort based on concatenation order
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Sort using custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Edge case: If the largest number is "0", return "0"
        if nums[0] == "0":
            return "0"
        
        return "".join(nums)
