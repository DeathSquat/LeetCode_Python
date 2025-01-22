class Solution:
    def solveNQueens(self, n):
        def is_safe(row, col):
            # Check if placing a queen at (row, col) is safe
            return not (cols[col] or diag1[row - col + n - 1] or diag2[row + col])

        def place_queen(row, col):
            # Place a queen at (row, col)
            board[row][col] = 'Q'
            cols[col] = True
            diag1[row - col + n - 1] = True
            diag2[row + col] = True

        def remove_queen(row, col):
            # Remove a queen from (row, col)
            board[row][col] = '.'
            cols[col] = False
            diag1[row - col + n - 1] = False
            diag2[row + col] = False

        def backtrack(row):
            if row == n:
                # All queens are placed, add the current board configuration
                solutions.append([''.join(row) for row in board])
                return

            for col in range(n):
                if is_safe(row, col):
                    place_queen(row, col)
                    backtrack(row + 1)
                    remove_queen(row, col)

        # Initialize variables
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = [False] * n  # Tracks if a column is under attack
        diag1 = [False] * (2 * n - 1)  # Tracks if a "/" diagonal is under attack
        diag2 = [False] * (2 * n - 1)  # Tracks if a "\" diagonal is under attack
        solutions = []

        # Start backtracking from the first row
        backtrack(0)

        return solutions
