from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque()

        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    if (
                        row == 0
                        or row == rows - 1
                        or col == 0
                        or col == cols - 1
                    ):
                        board[row][col] = "S"
                        queue.append((row, col))

        while queue:
            row, col = queue.popleft()

            up = (row - 1, col)
            down = (row + 1, col)
            left = (row, col - 1)
            right = (row, col + 1)

            neighbors = [up, down, left, right]

            for new_row, new_col in neighbors:
                if (
                    new_row < 0
                    or new_row >= rows
                    or new_col < 0
                    or new_col >= cols
                ):
                    continue

                if board[new_row][new_col] != "O":
                    continue

                board[new_row][new_col] = "S"
                queue.append((new_row, new_col))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"

