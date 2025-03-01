class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1:
            return 0

        # Step 1: Precompute the palindrome table
        is_palindrome = [[False] * n for _ in range(n)]
        
        for length in range(n):
            for start in range(n - length):
                end = start + length
                if s[start] == s[end]:
                    if length <= 1:
                        is_palindrome[start][end] = True
                    else:
                        is_palindrome[start][end] = is_palindrome[start + 1][end - 1]

        # Step 2: DP to find the minimum cuts
        dp = [float('inf')] * n
        
        for i in range(n):
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if is_palindrome[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]
