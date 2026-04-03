class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)

        if n == 0 or any(len(row) != n for row in board):
            return False

        subsquare = math.isqrt(n)

        if subsquare * subsquare != n:
            return False

        for row in range(n):
            seen = set()
            for col in range(n):
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        for col in range(n):
            seen = set()
            for row in range(n):
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        for square in range(n):
            seen = set()
            for i in range(subsquare):
                for j in range(subsquare):
                    row = (square//subsquare) * subsquare + i
                    col = (square%subsquare) * subsquare + j

                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True

