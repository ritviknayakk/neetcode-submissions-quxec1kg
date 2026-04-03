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
                for j in range(subsquare):                      # * subsquare tells us which grid we are in when going through the whole square sequence, it will be 0 * 3 for the first level(i.e 0,1,2), then 1*3 for second level(i.e 3,4,5)
                    row = (square // subsquare) * subsquare + i     # Floor division keeps the row constant as 0 0 0, 1 1 1, 2 2 2
                    col = (square % subsquare) * subsquare + j      # Modulus will keep changing the column values  0 1 2, 0 1 2, 0 1 2 
                                                                    # So 0th row stays constant while column changes for each subsquare
                    if board[row][col] == ".":
                        continue

                    if board[row][col] in seen:
                        return False

                    seen.add(board[row][col])

        return True