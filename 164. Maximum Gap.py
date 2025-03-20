class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        
        # Find the min and max value in nums
        min_val, max_val = min(nums), max(nums)
        
        if min_val == max_val:
            return 0  # All numbers are the same, so max gap is 0

        # Calculate bucket size and number of buckets
        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        # Initialize buckets with None (to track min and max in each bucket)
        buckets = [[None, None] for _ in range(bucket_count)]
        
        # Place numbers into buckets
        for num in nums:
            index = (num - min_val) // bucket_size
            if buckets[index][0] is None:
                buckets[index][0] = num  # Min in bucket
                buckets[index][1] = num  # Max in bucket
            else:
                buckets[index][0] = min(buckets[index][0], num)
                buckets[index][1] = max(buckets[index][1], num)
        
        # Compute max gap
        max_gap = 0
        prev_max = min_val
        
        for bucket in buckets:
            if bucket[0] is None:
                continue  # Skip empty buckets
            max_gap = max(max_gap, bucket[0] - prev_max)
            prev_max = bucket[1]
        
        return max_gap
