class Solution:
    # Max Abs Dif (Accepted), O(n) time, O(1) space
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points) - 1):
            coord1 = points[i]
            coord2 = points[i + 1]
            diff_x = coord2[0] - coord1[0]
            diff_y = coord2[1] - coord1[1]
            res += max(abs(diff_x), abs(diff_y))
        return res

    # # Larger Value of Absolute Differences (Top Voted), O(n) time, O(1) space
    # def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    #     ans = 0
    #     for i in range(1, len(points)):
    #         prev, cur = points[i - 1 : i + 1]
    #         ans += max(map(abs, (prev[0] - cur[0], prev[1] - cur[1])))
    #     return ans
