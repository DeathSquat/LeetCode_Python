class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for i in range(rows):
            # Update heights array
            for j in range(cols):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            
            # Compute max area in histogram
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        max_area = 0
        heights.append(0)  # Sentinel to ensure stack is emptied at the end

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)

        return max_area
