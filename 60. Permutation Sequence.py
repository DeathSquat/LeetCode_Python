class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial
        
        # Create a list of numbers from 1 to n
        numbers = list(range(1, n + 1))
        result = []
        k -= 1  # Convert k to 0-based index
        
        # Generate the permutation
        for i in range(n, 0, -1):
            # Determine the index of the current digit
            idx = k // factorial(i - 1)
            result.append(str(numbers[idx]))
            # Remove the used number
            numbers.pop(idx)
            # Update k
            k %= factorial(i - 1)
        
        return ''.join(result)
