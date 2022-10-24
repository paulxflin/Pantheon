class Solution:
    # Sets (Accepted), O(NW) time, O(1) space, N = number of words, W = length of longest word
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        A = set(allowed)
        res = 0
        for word in words:
            S = set(word)
            res += S.issubset(A)
        return res

    # One Liner (Top Voted), O(NW) time, O(1) space
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(all(c in allowed for c in w) for w in words)
