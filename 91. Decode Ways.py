class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':  
            return 0  # Invalid if it starts with '0'

        n = len(s)
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1  # Base cases

        for i in range(1, n):
            if s[i] != '0':  
                dp[i + 1] += dp[i]  # Single-digit decode
            
            two_digit = int(s[i - 1:i + 1])
            if 10 <= two_digit <= 26:  
                dp[i + 1] += dp[i - 1]  # Two-digit decode
        
        return dp[n]
