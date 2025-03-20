class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0:
            return str(numerator // denominator)

        res = []
        
        # Handle negative sign
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')

        # Convert to positive
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Integer part
        res.append(str(numerator // denominator))
        res.append('.')

        # Remainder map to detect cycles
        remainder_map = {}
        remainder = numerator % denominator
        
        while remainder and remainder not in remainder_map:
            remainder_map[remainder] = len(res)  # Store the position
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        # If remainder repeats, insert parentheses
        if remainder in remainder_map:
            idx = remainder_map[remainder]
            res.insert(idx, '(')
            res.append(')')

        return ''.join(res)
