class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Define constants for 32-bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle edge cases
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        if dividend == INT_MIN and divisor == 1:
            return INT_MIN

        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # Convert dividend and divisor to positive
        dividend, divisor = abs(dividend), abs(divisor)

        # Initialize quotient
        quotient = 0

        # Perform division using subtraction
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= temp:
                dividend -= temp
                quotient += multiple

                # Optimize by doubling temp and multiple
                if temp <= INT_MAX >> 1:
                    temp += temp
                    multiple += multiple

        # Apply the sign to the quotient
        quotient = -quotient if negative else quotient

        # Clamp the result to the 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, quotient))
