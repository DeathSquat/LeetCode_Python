class Solution(object):
    def isMatch(self, s, p):
        """
        :type s:str
        :type p:str
        :rtype:bool
        """
        m, n = len(s), len(p)

        # Create a DP table
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # Base case: empty string matches empty pattern

        # Handle patterns with '*' that can match zero preceding characters
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    # Characters match or pattern has '.'
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # '*' Matches zero or more of the preceding element
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

        return dp[m][n]
