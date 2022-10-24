class Solution:
    # One Liner (Accepted + Top Voted), O(n log n) time, O(n) space, where n = rows * cols
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        return sorted([[i, j] for i in range(rows) for j in range(cols)], key=lambda c: abs(c[0]-rCenter) + abs(c[1] - cCenter))
