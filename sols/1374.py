class Solution:
    # Mod 2 if-else (Accepted), O(n) time and space
    def generateTheString(self, n: int) -> str:
        if n % 2:
            return "a"*n
        else:
            return "a"*(n-1) + "b"

    # One Liner with bitwise and (Top Voted), O(n) time and space
    def generateTheString(self, n: int) -> str:
        return 'b' + 'ab'[n & 1] * (n - 1)
