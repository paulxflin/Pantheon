class Solution:
    # Brute Force (Accepted), O(n*m) time, O(1) space
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        s = set(list(range(1, 10)))

        def is_magic_square(i, j):
            sq = set()
            for r in range(i, i+3):
                for c in range(j, j+3):
                    sq.add(grid[r][c])

            r1 = sum(grid[i][c] for c in range(j, j+3))
            r2 = sum(grid[i+1][c] for c in range(j, j+3))
            r3 = sum(grid[i+2][c] for c in range(j, j+3))
            c1 = sum(grid[r][j] for r in range(i, i+3))
            c2 = sum(grid[r][j+1] for r in range(i, i+3))
            c3 = sum(grid[r][j+2] for r in range(i, i+3))
            d1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
            d2 = grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2]
            return r1 == r2 == r3 == c1 == c2 == c3 == d1 == d2 and sq == s

        for i in range(rows-2):
            for j in range(cols-2):
                if is_magic_square(i, j):
                    res += 1
        return res

    # Middle 5 and Surrounding 43816729 (Top Voted), O(n*m) time, O(1) space
    def numMagicSquaresInside(self, g: List[List[int]]) -> int:
        def isMagic(i, j):
            s = "".join(str(g[i + x // 3][j + x % 3])
                        for x in [0, 1, 2, 5, 8, 7, 6, 3])
            return g[i][j] % 2 == 0 and (s in "43816729" * 2 or s in "43816729"[::-1] * 2)
        return sum(isMagic(i, j) for i in range(len(g) - 2) for j in range(len(g[0]) - 2) if g[i + 1][j + 1] == 5)
