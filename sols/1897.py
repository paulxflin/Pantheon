import collections


class Solution:
    # Counter with defaultdict, O(n) time and space
    def makeEqual(self, words: List[str]) -> bool:
        counter = collections.defaultdict(int)
        for word in words:
            for c in word:
                counter[c] += 1
        n = len(words)
        for k in counter:
            if counter[k] % n != 0:
                return False
        return True

    # One Liner (Top Voted), O(n) time and space
    def makeEqual(self, w: List[str]) -> bool:
        return all(val % len(w) == 0 for val in collections.Counter(''.join(w)).values())
