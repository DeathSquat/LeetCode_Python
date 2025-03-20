class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] < nums[right]:  
                right = mid  # Minimum is in the left part
            elif nums[mid] > nums[right]:  
                left = mid + 1  # Minimum is in the right part
            else:  
                right -= 1  # Reduce search space safely
        
        return nums[left]
