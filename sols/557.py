class Solution:
    # Split, Reverse, then Join (Accepted), O(n) time and space
    def reverseWords(self, s: str) -> str:
        return " ".join([s[::-1] for s in s.split(" ")])

    # Double Reverse (Top Voted), O(n) time and space
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])[::-1]
