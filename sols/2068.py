from collections import Counter


class Solution:
    # Sets and Counter (Accepted), O(n) time, O(1) space
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        for k in set(word1 + word2):
            if abs(c1[k] - c2[k]) > 3:
                return False
        return True

    # One Liner (Top Voted), O(n) time, O(1) space
    def checkAlmostEquivalent(self, w1: str, w2: str) -> bool:
        return all(v < 4 for v in ((Counter(w1)-Counter(w2))+(Counter(w2)-Counter(w1))).values())
