class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Edge case: if either number is "0", the product is "0"
        if num1 == "0" or num2 == "0":
            return "0"

        # Initialize result array to store intermediate results
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Perform multiplication digit by digit
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Multiply digits and add to the corresponding position
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                pos1, pos2 = i + j, i + j + 1
                total = mul + result[pos2]

                # Update result array
                result[pos2] = total % 10
                result[pos1] += total // 10

        # Convert result array to string, skipping leading zeros
        result_str = ''.join(map(str, result)).lstrip('0')

        return result_str
