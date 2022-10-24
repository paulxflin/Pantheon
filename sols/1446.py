import itertools


class Solution:
    # One Pass (Accepted), O(n) time, O(1) space
    def maxPower(self, s: str) -> int:
        cnt = res = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cnt += 1
                res = max(cnt, res)
            else:
                cnt = 1
        return res

    # Itertools Groupby (Top Voted), O(n) time and space
    def maxPower(self, s: str) -> int:
        return max(len(list(b)) for a, b in itertools.groupby(s))
