from collections import Counter


class Solution:
    # Counter (Accepted), O(n) time and space
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    # Sort (Top Voted), O(n log n) time and space
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # Two Dicts (Top Voted), O(n) time and space
    def isAnagram(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2
