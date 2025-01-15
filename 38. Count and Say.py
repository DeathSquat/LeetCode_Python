class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def get_next(sequence):
            result = []
            count = 1
            for i in range(1, len(sequence)):
                if sequence[i] == sequence[i - 1]:
                    count += 1
                else:
                    result.append(str(count))
                    result.append(sequence[i - 1])
                    count = 1
            # Append the last group
            result.append(str(count))
            result.append(sequence[-1])
            return ''.join(result)
        
        current = "1"
        for _ in range(n - 1):
            current = get_next(current)
        
        return current

# Example usage:
solution = Solution()
print(solution.countAndSay(4))  # Output: "1211"
print(solution.countAndSay(1))  # Output: "1"
