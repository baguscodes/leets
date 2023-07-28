class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def is_safe(board, row, col):
            # Check if no queen attacks from the left side
            for i in range(col):
                if board[row][i] == 'Q':
                    return False

            # Check if no queen attacks from the upper-left diagonal
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False

            # Check if no queen attacks from the lower-left diagonal
            for i, j in zip(range(row, n), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False

            return True

        def backtrack(board, col):
            if col == n:
                result.append([''.join(row) for row in board])
                return

            for row in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, col + 1)
                    board[row][col] = '.'

        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(board, 0)
        return result