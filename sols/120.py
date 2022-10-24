class Solution:
    # Top Down DP (Accepted), O(n^2) time, O(1) space
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            row = triangle[i]
            row[0] += triangle[i-1][0]
            row[-1] += triangle[i-1][-1]
            for j in range(1, len(row)-1):
                row[j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])

    # Bottom Up DP (Top Voted), O(n^2) time, O(1) space
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
