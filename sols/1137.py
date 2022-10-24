class Solution:
    # # Iterative Solution (Accepted), O(n) time, O(1) space
    # def tribonacci(self, n: int) -> int:
    #     A = [0, 1, 1]
    #     if n < 3:
    #         return A[n]
    #     r = None
    #     for i in range(3, n+1):
    #         r = sum(A)
    #         A[0], A[1], A[2] = A[1], A[2], r
    #     return r

    # # Recursive with Memo (Accepted), O(n) time and space
    # def tribonacci(self, n: int) -> int:
    #     memo = {0:0, 1:1, 2:1}
    #     def tri(n):
    #         if n < 3:
    #             return memo[n]
    #         if n in memo:
    #             return memo[n]
    #         else:
    #             res = tri(n-3) + tri(n-2) + tri(n-1)
    #             memo[n] = res
    #             return res

    #     return tri(n)

    # # Iterative (Top Voted), O(n) time and space
    # def tribonacci(self, n: int) -> int:
    #     a, b, c = 1, 0, 0
    #     for _ in range(n): a, b, c = b, c, a + b + c
    #     return c

    # Bottom Up DP (Top Voted), O(n) time, O(1) space
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            dp[i % 3] = sum(dp)
        return dp[n % 3]
