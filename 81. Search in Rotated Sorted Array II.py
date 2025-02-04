class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True  # Target found

            # Handle duplicates by shrinking the search space
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:  # Target in left half
                    right = mid - 1
                else:  # Target in right half
                    left = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:  # Target in right half
                    left = mid + 1
                else:  # Target in left half
                    right = mid - 1

        return False  # Target not found
