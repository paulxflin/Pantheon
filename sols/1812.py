class Solution:
    # Steps from a1 (Accepted), O(1) time and space
    def squareIsWhite(self, C: str) -> bool:
        steps = ord(C[0]) - ord('a') + int(C[1]) - 1
        return steps % 2

    # One Liner (Top Voted), O(1) time and space
    def squareIsWhite(self, a):
        return ord(a[0]) % 2 != int(a[1]) % 2
