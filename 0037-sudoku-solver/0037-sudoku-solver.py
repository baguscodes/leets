class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def is_valid(num, row, col):
            for i in range(9):
                if board[i][col] == num or board[row][i] == num:
                    return False

            sub_box_row = (row // 3) * 3
            sub_box_col = (col // 3) * 3

            for i in range(3):
                for j in range(3):
                    if board[sub_box_row + i][sub_box_col + j] == num:
                        return False

            return True

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in map(str, range(1, 10)):
                            if is_valid(num, i, j):
                                board[i][j] = num
                                if solve():
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        solve()
