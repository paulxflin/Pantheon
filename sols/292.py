class Solution:
    # Pattern Recognition (Accepted + Top Voted), O(1) time and space
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
