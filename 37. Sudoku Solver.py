class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def is_valid(board, row, col, num):
            for i in range(9):
                # Check row and column
                if board[row][i] == num or board[i][col] == num:
                    return False
                # Check 3x3 sub-box
                box_row = 3 * (row // 3) + i // 3
                box_col = 3 * (col // 3) + i % 3
                if board[box_row][box_col] == num:
                    return False
            return True
        
        def find_empty_cell_with_fewest_options():
            # Find the empty cell with the fewest valid options to speed up backtracking
            min_options = 10  # Start with an impossible number of options (1-9)
            best_cell = None
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        options = sum(1 for num in map(str, range(1, 10)) if is_valid(board, i, j, num))
                        if options < min_options:
                            min_options = options
                            best_cell = (i, j)
                            # Early exit: if we find a cell with 1 option, prioritize it
                            if min_options == 1:
                                return best_cell
            return best_cell

        def backtrack():
            # Find the best cell to fill next
            empty_cell = find_empty_cell_with_fewest_options()
            if not empty_cell:
                return True  # No empty cells left, puzzle solved
            
            row, col = empty_cell
            for num in map(str, range(1, 10)):
                if is_valid(board, row, col, num):
                    board[row][col] = num
                    if backtrack():
                        return True
                    board[row][col] = '.'  # Undo the move if it leads to a dead end
            
            return False

        backtrack()

# Example usage:
board = [
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "9", ".", ".", "1", ".", ".", "3", "."],
    [".", ".", "6", ".", "2", ".", "7", ".", "."],
    [".", ".", ".", "3", ".", "4", ".", ".", "."],
    ["2", "1", ".", ".", ".", ".", ".", "9", "8"],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "2", "5", ".", "6", "4", ".", "."],
    [".", "8", ".", ".", ".", ".", ".", "1", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]
]

solution = Solution()
solution.solveSudoku(board)
print(board)
