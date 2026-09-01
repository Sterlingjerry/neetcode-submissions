class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        minutes = 0

        while queue and fresh > 0:
            level_size = len(queue)

            for i in range(level_size):
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
                    
                    if grid[new_row][new_col] != 1:
                        continue

                    grid[new_row][new_col] = 2
                    fresh -= 1
                    queue.append((new_row, new_col))

                    # check up/down/left/right
                    # rot fresh neighbors
                    # add newly rotten oranges to queue

            minutes += 1
        return minutes if fresh == 0 else -1
                        