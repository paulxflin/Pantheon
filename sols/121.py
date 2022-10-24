class Solution:
    # # Kandane's Algorithm (Top Voted), O(n) time, O(1) space
    # def maxProfit(self, prices: List[int]) -> int:
    #     max_cur, max_so_far = 0, 0
    #     for i in range(1, len(prices)):
    #         max_cur += prices[i] - prices[i-1]
    #         max_cur = max(0, max_cur)
    #         max_so_far = max(max_cur, max_so_far)
    #     return max_so_far

    # One Pass Optimised DP (Accepted + Solution), O(n) time, O(1) space
    def maxProfit(self, prices: List[int]) -> int:
        min_left = prices[0]
        max_profit = 0
        for i in prices[1:]:
            profit = i - min_left
            if profit > max_profit:
                max_profit = profit
            if i < min_left:
                min_left = i
        return max_profit
