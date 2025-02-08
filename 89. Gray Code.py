class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(n):
            result += [(1 << i) | x for x in reversed(result)]
        return result
