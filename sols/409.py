from collections import Counter


class Solution:
    # Count number of pairs with odd flag (Accepted), O(n) time and space
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        odd = res = 0
        for count in counts.values():
            if not odd and count % 2:
                odd = 1
            res += count // 2
        return 2 * res + odd

    # Count number of odds (Top Voted), O(n) time and space
    def longestPalindrome(self, s: str) -> int:
        odds = sum(v & 1 for v in Counter(s).values())
        return len(s) - odds + bool(odds)
