import operator


class Solution:
    # Brute Force (Accepted), O(m*n) time, O(1) space
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res += 4
                    if i - 1 >= 0 and grid[i-1][j]:
                        res -= 1
                    if i+1 < m and grid[i+1][j]:
                        res -= 1
                    if j-1 >= 0 and grid[i][j-1]:
                        res -= 1
                    if j+1 < n and grid[i][j+1]:
                        res -= 1
        return res

    # One Liner (Top Voted), O(m*n) time and space
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return sum(sum(map(operator.ne, [0] + row, row + [0])) for row in grid + list(map(list, zip(*grid))))

    # Faster One Liner (Accepted + Top Voted), O(m*n) time and space
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return sum(sum(map(operator.ne, [0] + row, row + [0])) for row in grid) + sum(sum(map(operator.ne, [0] + col, col + [0])) for col in map(list, zip(*grid)))

    # Logical Short Circuit (Top Voted), O(m * n) time, O(1) space
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perim = 0
        h, w = len(grid), len(grid[0])

        # Iterate through each cell
        for row in range(0, h):
            for col in range(0, w):

                # Is this a land cell?
                if grid[row][col] == 1:

                    # Top edge
                    if row == 0 or grid[row - 1][col] == 0:
                        perim += 1

                    # Bottom edge
                    if row == h - 1 or grid[row + 1][col] == 0:
                        perim += 1

                    # Left edge
                    if col == 0 or grid[row][col - 1] == 0:
                        perim += 1

                    # Right edge
                    if col == w - 1 or grid[row][col + 1] == 0:
                        perim += 1

        return perim
