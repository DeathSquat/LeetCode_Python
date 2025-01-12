class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        stack = [-1]  # Initialize stack with a base index
        
        for i in range(len(s)):
            if s[i] == '(':
                # Push the index of '(' onto the stack
                stack.append(i)
            else:
                # Pop the last index from the stack
                stack.pop()
                if not stack:
                    # If the stack is empty, push the current index
                    stack.append(i)
                else:
                    # Calculate length of the current valid substring
                    max_length = max(max_length, i - stack[-1])
        
        return max_length
