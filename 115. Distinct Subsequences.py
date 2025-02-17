class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        
        # Create a DP table where dp[i][j] represents the number of ways
        # to form t[0:j] from s[0:i]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # If t is an empty string, there is exactly one subsequence in s that matches it (empty subsequence)
        for i in range(m + 1):
            dp[i][0] = 1

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If characters match, we can either include this character or exclude it
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # Otherwise, we just exclude it
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]
