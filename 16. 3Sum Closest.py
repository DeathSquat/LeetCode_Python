class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Sort the array to facilitate the two-pointer technique
        nums.sort()
        closest_sum = float('inf')
        
        # Iterate through the array to fix the first element of the triplet
        for i in range(len(nums) - 2):
            # Initialize two pointers for the remaining part of the array
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update the closest sum if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on the comparison with the target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # If the current_sum is exactly equal to the target, return it
                    return current_sum
        
        return closest_sum
