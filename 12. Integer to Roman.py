class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Define mappings of integer values to Roman numerals
        value_to_roman = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        # Initialize the result Roman numeral string
        result = ""

        # Convert the integer to Roman numeral
        for value, roman in value_to_roman:
            while num >= value:
                result += roman
                num -= value

        return result