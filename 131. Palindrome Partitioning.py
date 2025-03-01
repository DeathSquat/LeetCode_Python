class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.backtrack(s, 0, [], result)
        return result

    def backtrack(self, s, start, path, result):
        if start == len(s):
            result.append(list(path))
            return
        
        for end in range(start, len(s)):
            if self.is_palindrome(s, start, end):
                path.append(s[start:end+1])
                self.backtrack(s, end + 1, path, result)
                path.pop()

    def is_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
