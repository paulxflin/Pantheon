class Solution:
    # # Buy at Valley, Sell at Peak (Accepted), O(n) time, O(1) space
    # def maxProfit(self, prices: List[int]) -> int:
    #     sz = len(prices)
    #     if sz < 2:
    #         return 0
    #     buy, profit = None, 0
    #     for i in range(sz-1):
    #         if buy is not None:  # We're looking to sell
    #             if prices[i] > buy and prices[i] >= prices[i+1]:
    #                 profit += prices[i] - buy
    #                 buy = None
    #         else:  # We want to buy
    #             if prices[i] < prices[i+1]:
    #                 buy = prices[i]
    #     if buy is not None and prices[sz-1] > buy:
    #         profit += prices[sz-1] - buy
    #     return profit

    # Simple One Pass Peak Valley One Liner (Top Voted), O(n) time, O(1) space
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
