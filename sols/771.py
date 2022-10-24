class Solution:
    # Set of Jewels and Sum (Accepted), O(J+S) time, O(J) space
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        S = set(list(jewels))
        res = 0
        for c in stones:
            if c in S:
                res += 1
        return res

    # Set of Jewels and Sum (Top Voted), O(J+S) time, O(J) space
    def numJewelsInStones(self, J: str, S: str) -> int:
        setJ = set(J)
        return sum(s in setJ for s in S)
