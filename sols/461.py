class Solution:
    # One Liner (Accepted + Top Voted), O(1) time and space (due to 32 bit)
    def hammingDistance(self, x: int, y: int) -> int:
        return "{0:b}".format(x ^ y).count('1')

    # Bitwise and (Top Voted), O(1) time and space
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        num_ones = 0
        while n > 0:
            n &= (n-1)
            num_ones += 1
        return num_ones
