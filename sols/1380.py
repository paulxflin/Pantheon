class Solution:
    # Set intersection (Accepted), O(m * n) time, O(m + n) space
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        min_row = set(min(row) for row in matrix)
        max_col = set(max(matrix[i][j] for i in range(rows))
                      for j in range(cols))
        return min_row & max_col

    # One Liner (Top Voted), O(m * n) time, O(m + n) space
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        return list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)})
