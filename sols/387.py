from collections import Counter


class Solution:
    # Iterating Counter (Accepted), O(n) time, O(1) space
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for c in counter:
            if counter[c] == 1:
                return s.index(c)
        return -1

    # Linear Time iterating String (Solution), O(n) time, O(1) space
    def firstUniqChar(self, s: str) -> int:
        # build hash map : character and how often it appears
        count = Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1

    # 3 Liner reliant on C-functions (Top Voted), O(n) time, O(1) space
    def firstUniqChar(self, s: str) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
