from itertools import accumulate


class Solution:
    # Track running sum (Accepted), O(n) time, O(1) space
    def minStartValue(self, nums: List[int]) -> int:
        min_run = 0
        run = 0
        for n in nums:
            run += n
            min_run = min(min_run, run)
        return max(1-min_run, 1)

    # Running Sum accounting for default (Top Voted), O(n) time, O(1) space
    def minStartValue(self, A: List[int]) -> int:
        Sum, ans = 0, 0
        for el in A:
            Sum = Sum + el
            ans = min(ans, Sum)
        return -ans + 1

    # One Liner (Top Voted), O(n) time, O(1) space
    def minStartValue(self, A: List[int]) -> int:
        return -min(0, min(accumulate(A))) + 1
