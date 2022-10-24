from collections import Counter


class Solution:
    # Two Liner (Accepted), O(m+n) time and space
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc, mc = Counter(ransomNote), Counter(magazine)
        return not rc-mc

    # One Liner (Top Voted), O(m+n) time and space
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)
