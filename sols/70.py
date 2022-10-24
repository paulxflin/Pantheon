class Solution:
    # # DP (Accepted), O(n) time, O(n) space
    # def climbStairs(self, n: int) -> int:
    #     ways = [1, 1]
    #     if n < 2:
    #         return ways[n]
    #     for i in range(2, n+1):
    #         ways.append(ways[i-1] + ways[i-2])
    #     return ways[n]

    # Optimised DP (Accepted), O(n) time, O(1) space
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        a = b = 1
        for i in range(2, n+1):
            a, b = b, a + b
        return b

    # # Optimised DP (Top Voted), O(n) time, O(1) space
    # def climbStairs(self, n: int) -> int:
    #     a = b = 1
    #     for _ in range(n):
    #         a, b = b, a + b
    #     return a
