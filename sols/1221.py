class Solution:
    # Increment res, n to track L - R (Accepted), O(n) time, O(1) space
    def balancedStringSplit(self, s: str) -> int:
        n = 0
        res = 0
        for c in s:
            if c == 'L':
                n -= 1
            else:
                n += 1
            if n == 0:
                res += 1
        return res

    # # Increment res for equal L and R (Top Voted), O(n) time, O(1) space
    # def balancedStringSplit(self, s: str) -> int:
    #     res = cnt = 0
    #     for c in s:
    #         cnt += 1 if c == 'L' else -1
    #         if cnt == 0:
    #             res += 1
    #     return res
