class Solution:
    # # Subtract first and mod 2 (Accepted), O(n) time, O(1) space
    # def minCostToMoveChips(self, position: List[int]) -> int:
    #     res, n = 0, len(position)
    #     if n < 2:
    #         return 0
    #     base = position[0]
    #     for i in range(n):
    #         res += (position[i] - base) % 2

    #     return res if res <= n/2 else n-res

    # Odd/Even approach (Top Voted), O(n) time, O(1) space
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odds = sum(x % 2 for x in chips)
        return min(odds, len(chips) - odds)
