class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)

        # Create a DP table where dp[i][j] indicates if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string and empty pattern match
        dp[0][0] = True

        # Handle patterns with '*' at the start
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    # Characters match or '?' matches any character
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # '*' matches zero characters (dp[i][j-1]) or one/more characters (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        # Final result is whether the entire string matches the pattern
        return dp[m][n]
