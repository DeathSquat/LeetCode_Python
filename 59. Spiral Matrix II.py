class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]  # Initialize an n x n matrix with zeros
        left, right, top, bottom = 0, n - 1, 0, n - 1  # Boundaries
        num = 1  # Start filling from 1
        
        while left <= right and top <= bottom:
            # Fill top row
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1  # Move the top boundary down
            
            # Fill right column
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1  # Move the right boundary left
            
            # Fill bottom row
            if top <= bottom:  # Check to prevent overwriting
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1  # Move the bottom boundary up
            
            # Fill left column
            if left <= right:  # Check to prevent overwriting
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1  # Move the left boundary right
        
        return matrix
