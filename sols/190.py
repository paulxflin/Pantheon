class Solution:
    # Reverse Format String (Accepted), O(1) time and space
    def reverseBits(self, n: int) -> int:
        s = '{:032b}'.format(n)[::-1]
        return int(s, 2)

    # Bit Manipulation (Top Voted), O(1) time and space
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans
