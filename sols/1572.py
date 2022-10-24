class Solution:
    # Sum both diagonals and remove overlap (Accepted + Top Voted), O(n) time, O(1) space
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for i in range(n):
            res += mat[i][i] + mat[i][n-1-i]
        if n % 2:
            mid = n//2
            return res - mat[mid][mid]
        return res
