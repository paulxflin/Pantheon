class Solution:
    # For loop (Accepted), O(n) time, O(1) space
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for pattern in patterns:
            if pattern in word:
                res += 1
        return res

    # One liner LC (Top Voted), O(n) time, O(1) space
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(x in word for x in patterns)
