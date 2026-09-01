from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
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
                    or new_row >= len(grid)
                    or new_col < 0
                    or new_col >= len(grid[0])
                ):
                    continue

                if grid[new_row][new_col] != INF:
                    continue

                grid[new_row][new_col] = grid[row][col] + 1
                queue.append((new_row, new_col))