class Solution(object):
    # # Brute Force (Accepted), Time: O(n * m), Space: O(1)
    # def countNegatives(self, grid):
    #     """
    #     :type grid: List[List[int]]
    #     :rtype: int
    #     """
    #     total = 0
    #     for row in grid:
    #         for item in row:
    #             if item < 0:
    #                 total += 1
    #     return total

    # # Binary Search (Top Voted), Time O(m log n), Space O(1)
    # def countNegatives(self, grid):
    #     def bin(row):
    #         start, end = 0, len(row)
    #         while start<end:
    #             mid = start +(end - start) // 2  # Start Index + 0.5 range
    #             if row[mid]<0:
    #                 end = mid
    #             else:
    #                 start = mid+1
    #         return len(row)- start

    #     count = 0
    #     for row in grid:
    #         count += bin(row)
    #     return(count)

    # Staircase (Top Voted), Time O(m + n), Space O(1)
    def countNegatives(self, grid):
        # m is the row length, n is the column length
        m, n = len(grid), len(grid[0])
        r, c, cnt = m - 1, 0, 0  # Starts from Bottom Left Corner
        while r >= 0 and c < n:  # Bottom to top row, left to right column
            if grid[r][c] < 0:
                cnt += n - c
                r -= 1
            else:
                c += 1
        return cnt
