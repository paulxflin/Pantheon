from collections import Counter


class Solution:
    # Counter Operators (Accepted), O(n) time and space
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        cnt = Counter(
            ''.join([c for c in licensePlate.lower() if c.isalpha()]))
        ans = None
        for word in words:
            cntw = Counter(word)
            if not (cnt - cntw) and (not ans or len(word) < len(ans)):
                ans = word
        return ans

    # Two Liner (Top Voted), O(n) time and space
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        pc = Counter(filter(lambda x: x.isalpha(), licensePlate.lower()))
        return min([w for w in words if Counter(w) & pc == pc], key=len)
