class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Determine if x is negative
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Reverse the integer
        reversed_x = 0
        while x != 0:
            pop = x % 10
            x //= 10

            # Check for overflow before appending the digit
            if reversed_x > (INT_MAX - pop) // 10:
                return 0

            reversed_x = reversed_x * 10 + pop

        return sign * reversed_x
