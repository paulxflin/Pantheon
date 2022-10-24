class Solution:
    # Grid Reduction without if-elif-else (Accepted), O(m*n) time, O(1) space
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        s = 0
        for i in range(m):
            grid[i][0] += s
            s = grid[i][0]
        s = 0
        for j in range(n):
            grid[0][j] += s
            s = grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

    # Grid Reduction (Top Voted), O(m*n) time, O(1) space
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) <= 0 or grid is None:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:  # We just want to skip the top-left corner of the grid
                    continue
                if r-1 < 0:  # Cases for elements in top row
                    grid[r][c] = grid[r][c] + grid[r][c-1]
                elif c-1 < 0:  # Cases for elements in leftmost column
                    grid[r][c] = grid[r][c] + grid[r-1][c]
                else:  # Normal cell
                    grid[r][c] = grid[r][c] + min(grid[r-1][c], grid[r][c-1])

        # We have got the minimum path accumaled at the bottom-right corner, just return this
        return grid[rows-1][cols-1]
