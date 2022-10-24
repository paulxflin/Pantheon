from collections import Counter


class Solution:
    # Counter (Accepted), O(n) time and space
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = 0
        for n in cnt:
            if cnt[n] == 1:
                res += n
        return res

    # One Liner (Top Voted), O(n) time and space
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(a for a, c in Counter(nums).items() if c == 1)
