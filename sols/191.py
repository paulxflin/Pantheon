class Solution:
    # Convert to Binary and Count (Accepted), O(n) time and space
    def hammingWeight(self, n: int) -> int:
        s = "{0:b}".format(n)
        return s.count('1')

    # Bit Operation (Top Voted), O(n) time, O(1) space
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c
