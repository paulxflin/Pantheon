class Solution:
    # # DP (Accepted), O(n) time and space
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     if len(cost) < 2:
    #         return 0
    #     dp = [None] * (len(cost) + 1)
    #     dp[0] = cost[0]
    #     dp[1] = cost[1]
    #     i = 2
    #     while i < len(cost):
    #         dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
    #         i += 1
    #     return min(dp[i-1], dp[i-2])

    # Bottom Up Memory Optimised (Top Voted), O(n) time, O(1) space
    def minCostClimbingStairs(self, A: List[int]) -> int:
        N = len(A)
        # memo +2 for base case: reached the top floor dp[N] or dp[N + 1]
        a, b, c = 0, 0, 0
        for i in range(N - 1, -1, -1):
            # as the recursive stack unwinds: cost of i-th step + min(one step, two steps)
            c = A[i] + min(b, a)
            a = b
            b = c                # slide window
        return min(b, a)  # minimal cost starting at first or second step

    # Bottom Up Solution Optimised (Accepted), O(n) time, O(1) space
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = b = c = 0
        for i in range(len(cost)):
            c = min(a, b) + cost[i]
            a, b = b, c
        return min(a, b)
