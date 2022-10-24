class Solution:
    # # Loop (Accepted), O(log n) time, O(1) space
    # def numberOfMatches(self, n: int) -> int:
    #     res = 0
    #     while n != 1:
    #         if n % 2 == 0:
    #             n //= 2
    #             res += n
    #         else:
    #             n //= 2
    #             res += n + 1
    #     return res

    # Intuition n-1 (Top Voted), O(1) time and space
    def numberOfMatches(self, n: int) -> int:
        return n-1
