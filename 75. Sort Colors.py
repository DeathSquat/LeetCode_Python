class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left, mid, right = 0, 0, len(nums) - 1

        while mid <= right:
            if nums[mid] == 0:  # Move 0s to the left
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:  # Keep 1s in the middle
                mid += 1
            else:  # Move 2s to the right
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
