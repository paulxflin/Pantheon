from collections import defaultdict
from itertools import count
from _operator import sub


class Solution:
    # Append new instance to list in dict (Accepted), O(n) time and space
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = defaultdict(list)
        for i in range(len(s)):
            d[s[i]].append(i)

        res = -1
        for v in d.values():
            dist = v[-1] - v[0] - 1
            res = max(dist, res)
        return res

    # One liner (Top Voted), O(n) time and space
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        return max(map(sub, count(), map({}.setdefault, s, count(1))))
