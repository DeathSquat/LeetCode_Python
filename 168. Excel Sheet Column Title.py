class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""
        while columnNumber > 0:
            columnNumber -= 1  # Adjusting for 0-based index
            result = chr(ord('A') + (columnNumber % 26)) + result
            columnNumber //= 26
        return result
