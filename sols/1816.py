class Solution:
    # Split, slice, join (Accepted + Top Voted), O(n) time and space
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])
