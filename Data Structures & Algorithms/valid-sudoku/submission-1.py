import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        # Ensure it's an n x n board
        if n == 0 or any(len(row) != n for row in board):
            return False

        subsquare = int(math.isqrt(n))

        # Ensure n is a perfect square (needed for valid subgrids)
        if subsquare * subsquare != n:
            return False

        # Check rows
        for row in range(n):
            seen = set()
            for col in range(n):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # Check columns
        for col in range(n):
            seen = set()
            for row in range(n):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # Check subgrids (same style as your original logic)
        for square in range(n):
            seen = set()
            for i in range(subsquare):
                for j in range(subsquare):
                    row = (square // subsquare) * subsquare + i
                    col = (square % subsquare) * subsquare + j

                    if board[row][col] == ".":
                        continue

                    if board[row][col] in seen:
                        return False

                    seen.add(board[row][col])

        return True