class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0

        def dfs(row, col):
            if (
                row < 0 or row>= len(grid)or
                col < 0 or col>= len(grid[row])or
                grid[row][col] == 0 or
                (row,col) in visited      
            ):
                return 0

            visited.add((row,col))

            up = dfs(row - 1, col)
            down = dfs(row + 1, col)
            left = dfs(row, col-1)
            right =dfs(row, col+1)

            return 1 + up + down + left + right
            
            

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max (max_area,dfs(row, col))

        return max_area