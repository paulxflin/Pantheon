class Solution:
    # Two Variables (Accepted), O(n) time, O(1) space
    def fib(self, n: int) -> int:
        a, b = 0, 1
        if n < 2:
            return n
        for _ in range(n-1):
            a, b = b, a + b
        return b

    # Tuple (Top Voted), O(n) time, O(1) space
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        memo = (0, 1)
        for _ in range(2, N+1):
            memo = (memo[-1], memo[-1] + memo[-2])
        return memo[-1]

    # Maths (Top Voted), O(n) time, O(1) space
    def fib(self, N):
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** N + 1) / 5 ** 0.5)
