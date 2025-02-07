class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Memoization dictionary
        memo = {}

        def dfs(s1, s2):
            # If already computed, return result
            if (s1, s2) in memo:
                return memo[(s1, s2)]

            # Base cases
            if s1 == s2:
                return True
            if sorted(s1) != sorted(s2):  # Quick pruning
                return False

            n = len(s1)
            for i in range(1, n):
                # Case 1: No swap
                if dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:]):
                    memo[(s1, s2)] = True
                    return True
                # Case 2: Swap
                if dfs(s1[:i], s2[-i:]) and dfs(s1[i:], s2[:-i]):
                    memo[(s1, s2)] = True
                    return True

            memo[(s1, s2)] = False
            return False

        return dfs(s1, s2)
